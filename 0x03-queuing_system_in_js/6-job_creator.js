const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '09068272767',
  message: 'This is a message',
}).save((err) => { if (err) console.log('Notification job failed'); else console.log('Notification job created:', job.id); })
  .on('complete', (val) => {
    console.log('Notification job completed');
  });
