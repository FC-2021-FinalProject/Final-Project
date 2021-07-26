    let currentDate = new Date(); 
    const $datepicker = document.querySelector('.date-picker > .date-picker-selector');
    const $calendar = document.querySelector('.date-picker > .calendar');

    const formattedDate = (() => {
      const format = n => (n < 10 ? '0' + n : n + '');
      return date => `${date.getFullYear()}-${format(date.getMonth() + 1)}-${format(date.getDate())}`;
    })();

    const renderCalendar = (() => {
      let size = 360; 

      const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December'];

      const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

      const eachCalendarDates = (() => {
        const diffDays = (from, to) => Math.abs(to - from) / 86400000;

        return (currentYear, currentMonth) => {
          const firstDay = new Date(currentYear, currentMonth, 1).getDay() + 1;
          const lastDay = new Date(currentYear, currentMonth + 1, 0).getDay() + 1;
          const from = new Date(currentYear, currentMonth, 1 - (firstDay - 1));
          const to = new Date(currentYear, currentMonth + 1, 7 - lastDay);

          return Array.from({ length: diffDays(from, to) + 1 }, (_, i) => {
            if (i) from.setDate(from.getDate() + 1); 
            return new Date(from); 
          });
        };
      })();

      const isEqualDate = (d1, d2) =>
        d1.getFullYear() === d2.getFullYear() &&
        d1.getMonth() === d2.getMonth() &&
        d1.getDate() === d2.getDate();

      return _size => {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        const classNames = date => {
          const today = new Date();
          const res = [];

          if (isEqualDate(date, today)) res.push('today');
          if (date.getMonth() !== month) res.push('muted');
          if (!date.getDay()) res.push('sunday');
          if (isEqualDate(date, currentDate)) res.push('selected');

          return res.join(' ');
        };

        $calendar.innerHTML = `
          <div class="calendar-nav">
            <i class="prev bx bx-caret-left"></i>
            <div class="calendar-title">
              <div class="month">${monthNames[month]}</div>
              <div class="year">${year}</div>
            </div>
            <i class="next bx bx-caret-right"></i>
          </div>
          <div class="calendar-grid">
            ${dayNames.map(day => `<div class="day">${day}</div>`).join('')}
            ${eachCalendarDates(year, month)
              .map(
                date =>
                  `<div data-date="${formattedDate(date)}" class="${classNames(date)}">
                    ${date.getDate()}
                  </div>`
              )
              .join('')}
          </div>`;

        size = _size ?? size;
        $calendar.style.setProperty('--calendar-width', `${size}px`);

        $calendar.style.display = 'block';
      };
    })();

    $calendar.onclick = e => {
      e.stopPropagation();

      if (e.target.classList.contains('prev')) {
        currentDate = new Date(
          currentDate.getFullYear(),
          currentDate.getMonth() - 1,
          currentDate.getDate()
        );
        $datepicker.value = formattedDate(currentDate);
        return renderCalendar();
      }
      if (e.target.classList.contains('next')) {
        currentDate = new Date(
          currentDate.getFullYear(),
          currentDate.getMonth() + 1,
          currentDate.getDate()
        );
        $datepicker.value = formattedDate(currentDate);
        return renderCalendar();
      }
      if (
        e.target.matches('.calendar > .calendar-grid > div:not(.day)') &&
        !e.target.classList.contains('selected')
      ) {
        document.querySelector('.selected')?.classList.remove('selected');
        e.target.classList.add('selected');

        console.log('[SELECTED DATE]', e.target.dataset.date);
        currentDate = new Date(e.target.dataset.date);
        $datepicker.value = e.target.dataset.date;

        $calendar.style.display = 'none';
      }
    };
    document.onclick = e => {
      if (e.target === $datepicker) return;
      $calendar.style.display = 'none';
    };

    $datepicker.onfocus = () => renderCalendar(300);