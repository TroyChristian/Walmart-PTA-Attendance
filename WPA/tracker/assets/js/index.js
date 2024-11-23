import { VanillaCalendar } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/build/vanilla-calendar.min.css';

document.addEventListener('DOMContentLoaded', () => {
    const calendar = new VanillaCalendar('#calendar', {
        settings: {
            selection: {
                day: 'multiple',
            },
            selected: {
                dates: ['2024-02-25', '2024-02-26'],
            },
        },
        actions: {
            clickDay(e, dates) {
                console.log('Selected dates:', dates);
            },
        },
    });
    calendar.init();
});
