
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc.js';
import timezone from 'dayjs/plugin/timezone.js';

let now = dayjs();
dayjs.extend(utc);
dayjs.extend(timezone);

const commonTimezones = [
    'Europe/London',
    'Europe/Paris',
    'America/New_York',
    'America/Los_Angeles',
    'Asia/Tokyo',
    'Asia/Shanghai',
    'Australia/Sydney',
    'GMT',
    'UTC',
]

const curTime = now.format('HH:mm:ss')
const curDate = now.format('dddd, D MMMM, YYYY');
const applyTimezoneButton = document.getElementById('apply-timezone');

let zone = localStorage.getItem('userTimezone') || dayjs.tz.guess();


const displayDiv = document.getElementById('time-display-container');
displayDiv.innerHTML = `
<div id="user-timezone">${zone}</div>
<div id="current-time">${curTime}</div>
<div id="current-date">${curDate}</div>`;

