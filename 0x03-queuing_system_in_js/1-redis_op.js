import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err))
  .on('ready', () => console.log('Redis client connected to the server'))
  .connect();

function setNewSchool(schoolName, value) {
  client.then((v) => {
    v.set(schoolName, value, print).then((res) => { console.log(res); });
  });
}

function displaySchoolValue(schoolName) {
  client.then((v) => {
    v.get(schoolName).then((res) => { console.log(res); });
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
