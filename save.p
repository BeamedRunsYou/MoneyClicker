const { Client, IntentsBitField, MessageEmbed } = require('discord.js');
const client = new Client({
    intents: [
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.GuildMembers
    ]
});

const urlRegex = /(https?:\/\/[^\s]+)/g;

const userMessageCount = new Map();
const recentMessages = new Map();
const actionLogs = [];

const MAX_MESSAGES_PER_INTERVAL = 5;
const INTERVAL_TIME = 10000;
const MESSAGE_COOLDOWN_TIME = 5000;

const JOIN_THRESHOLD = 5;
const JOIN_WINDOW = 60000;

client.once('ready', () => {
    console.log('Bot is online!');
});

client.on('messageCreate', async (message) => {
    if (message.author.bot) return;

    const userId = message.author.id;

    handleSpamProtection(message, userId);
    checkProfanity(message);
    checkForUrls(message);
    checkForMessageCooldown(message);
    handleDuplicateMessages(message);
});

function handleSpamProtection(message, userId) {
    const user = userMessageCount.get(userId) || { count: 0, lastMessageTime: Date.now() };

    const timeDifference = Date.now() - user.lastMessageTime;
    if (timeDifference > INTERVAL_TIME) {
        user.count = 1;
    } else {
        user.count++;
    }

    if (user.count > MAX_MESSAGES_PER_INTERVAL) {
        message.delete();
        message.reply("You're sending messages too quickly. Please slow down!");
        logAction('Spam Protection', message);
        return;
    }

    user.lastMessageTime = Date.now();
    userMessageCount.set(userId, user);
}

function checkProfanity(message) {
    const content = message.content.toLowerCase();
    if (filter.isProfane(content)) {
        message.delete();
        message.reply("Your message contains inappropriate language and has been deleted.");
        logAction('Profanity Detected', message);
    }
}

function checkForUrls(message) {
    const urls = message.content.match(urlRegex);
    if (urls) {
        message.delete();
        message.reply("Links are not allowed in this server.");
        logAction('URL Blocked', message);
    }
}

function checkForMessageCooldown(message) {
    const userCooldown = recentMessages.get(message.author.id);
    if (userCooldown && (Date.now() - userCooldown) < MESSAGE_COOLDOWN_TIME) {
        message.delete();
        message.reply("You're sending messages too quickly, please wait a moment.");
        logAction('Message Cooldown', message);
        return;
    }

    recentMessages.set(message.author.id, Date.now());
}

function handleDuplicateMessages(message) {
    const user = recentMessages.get(message.author.id) || { content: '', timestamp: Date.now() };

    if (user.content === message.content && Date.now() - user.timestamp < 3000) {
        message.delete();
        message.reply("Please don't repeat the same message.");
        logAction('Duplicate Message', message);
    } else {
        recentMessages.set(message.author.id, { content: message.content, timestamp: Date.now() });
    }
}

function logAction(action, message) {
    const logEmbed = new MessageEmbed()
        .setColor('#FF0000')
        .setTitle(`${action} - Log`)
        .addField('User:', `${message.author.tag} (${message.author.id})`)
        .addField('Channel:', message.channel.name)
        .addField('Message Content:', message.content)
        .setTimestamp();

    actionLogs.push(logEmbed);
    console.log(`[LOG] ${action} | User: ${message.author.tag} | Content: ${message.content}`);

    const logChannel = message.guild.channels.cache.find(ch => ch.name === 'moderator-only');
    if (logChannel) logChannel.send({ embeds: [logEmbed] });
}

client.on('guildMemberAdd', member => {
    const now = Date.now();
    const recentJoins = member.guild.members.cache.filter(m => (now - m.joinedTimestamp) < JOIN_WINDOW).size;

    if (recentJoins > JOIN_THRESHOLD) {
        const raidChannel = member.guild.channels.cache.find(ch => ch.name === 'moderator-only');
        if (raidChannel) {
            raidChannel.send("Warning: Potential raid detected! Multiple members joined within a short time.");
        }
        member.ban({ reason: 'Raid detection' }).catch(console.error);
    }
});
