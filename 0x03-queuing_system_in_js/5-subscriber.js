import { createClient } from 'redis';

const client = createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  })
  .connect();

const CHANNEL = 'holberton school channel';

client.subscribe(CHANNEL, (message, channel) => {
  if (channel === CHANNEL) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(CHANNEL);
      client.quit();
    }
  }
});
