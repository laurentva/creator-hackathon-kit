// Install MQTT library: npm install mqtt
const mqtt = require('mqtt');

const TOPIC = '5abca60f0e091b0005581409';
const USERNAME = TOPIC;
const API_KEY = '030d3ab9-df02-4213-83de-90b31b86920a';

const client = mqtt.connect('wss://mqtt.cloud.pozyxlabs.com:443', {
  username: USERNAME,
  password: API_KEY,
});

client.subscribe(TOPIC);
client.on('message', (topic, message) => {
  console.info(message.toString());
});