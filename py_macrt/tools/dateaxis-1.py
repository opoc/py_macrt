from pyqtgraph.graphicsItems.AxisItem import AxisItem
import time
from datetime import datetime
from pandas import date_range, DateOffset
from pandas.tseries.offsets import YearBegin, MonthBegin
from itertools import izip
import warnings
from dateutil.relativedelta import relativedelta


class DateAxis(AxisItem):
    
    def __init__(self, *args, **kwds):
        super(DateAxis, self).__init__(*args, **kwds)
    
    def tickValues(self, minVal, maxVal, size):
                
        minVal, maxVal = sorted((minVal, maxVal))
        
        # upon opening, we don't want any tick values
        if minVal == 0 and maxVal == 1:
            return [(0,[]), (0,[])]
        
        self._freqs = ['YEARLY', 'MONTHLY', 'DAILY', 'HOURLY', 'MINUTELY', 'SECONDLY']
        self.minticks = 5

        self.maxticks = {'YEARLY': 11, 'MONTHLY': 12, 'DAILY': 11, 'HOURLY': 12,
                         'MINUTELY': 11, 'SECONDLY': 11}
        self.interval_multiples = True
        self.intervald = {
            'YEARLY': [1, 2, 4, 5, 10, 20, 40, 50, 100],
            'MONTHLY': [1, 2, 3, 4, 6],
            'DAILY': [1, 2, 3, 7, 14],
            'HOURLY': [1, 2, 3, 4, 6, 12],
            'MINUTELY': [1, 5, 10, 15, 30],
            'SECONDLY': [1, 5, 10, 15, 30],
            }

        minDate = datetime.fromtimestamp(minVal)
        maxDate = datetime.fromtimestamp(maxVal)
        delta   = relativedelta(maxDate, minDate)

        numYears    = (delta.years * 1.0)
        numMonths   = (numYears * 12.0) + delta.months
        numDays     = (numMonths * 31.0) + delta.days
        numHours    = (numDays * 24.0) + delta.hours
        numMinutes  = (numHours * 60.0) + delta.minutes
        numSeconds  = (numMinutes * 60.0) + delta.seconds
        numMicroseconds = (numSeconds * 1e6) + delta.microseconds

        nums = [numYears, numMonths, numDays, numHours, numMinutes,
                numSeconds, numMicroseconds]

        for (freq, num) in izip(self._freqs, nums):
            # If this particular frequency doesn't give enough ticks, continue
            if num < self.minticks:
                continue

            # Find the first available interval that doesn't give too many
            # ticks
            for interval in self.intervald[freq]:
                if num <= interval * (self.maxticks[freq] - 1):
                    break
            else:
                # We went through the whole loop without breaking, default to
                # the last interval in the list and raise a warning
                warnings.warn('AutoDateLocator was unable to pick an '
                              'appropriate interval for this date range. '
                              'It may be necessary to add an interval value '
                              "to the AutoDateLocator's intervald dictionary."
                              ' Defaulting to {0}.'.format(interval))

            # Set some parameters as appropriate
            self._freq = freq

            break
        else:
            raise ValueError('No sensible date limit could be found')
        
        baseDate = datetime(minDate.year, minDate.month, minDate.day)
        if freq == 'YEARLY':
            offset = DateOffset(years=interval)
            majorTicks = date_range(baseDate + YearBegin(-1), maxDate, freq=offset)
        if freq == 'MONTHLY':
            offset = DateOffset(months=interval)
            majorTicks = date_range(baseDate + MonthBegin(-1), maxDate, freq=offset)
        if freq == 'WEEKLY':
            offset = DateOffset(weeks=interval)
            majorTicks = date_range(baseDate + DateOffset(days=-1), maxDate, freq=offset)
        if freq == 'DAILY':
            offset = DateOffset(days=interval)
            majorTicks = date_range(baseDate + DateOffset(days=-1), maxDate, freq=offset)
        if freq == 'HOURLY':
            offset = DateOffset(hours=interval)
            majorTicks = date_range(baseDate + DateOffset(days=-1), maxDate, freq=offset)
        
        majorTicks  = majorTicks.tz_localize('US/Eastern')
        ticks       = [ (0, majorTicks.asi8 / 1e9), (0,[])]
        return ticks


    def tickStrings(self, values, scale, spacing):
        
        strns = []
        if len(values) == 0:
            return strns
        
        formats = {
            'YEARLY': '%Y',
            'MONTHLY':  '%d%b%y',
            'WEEKLY':   '%d%b%y',
            'DAILY':    '%d%b%y',
            'HOURLY':   '%d%b%y %H',
            'MINUTELY': '%H:%M:%S.%f',
            'SECONDLY': '%H:%M:%S.%f',
        }
        
        fmt = formats[self._freq]
        
        for x in values:
            try:
                strns.append(time.strftime(fmt, time.localtime(x)))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')

        return strns
