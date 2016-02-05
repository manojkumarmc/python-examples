

class MyDate(object):
    def __init__(self, d, m, y):
        self.day = int(d)
        self.month = int(m)
        self.year = int(y)

    def __lt__(self, obj):
        ret_val = False
        if self.year < obj.year:
            ret_val = True
        else:
            if self.month < obj.month:
                ret_val = True
            elif self.month == obj.month:
                if self.day < obj.day:
                    ret_val = True
            else:
                if self.day < obj.day:
                    ret_val = True
        return ret_val

    def __eq__(self, obj):
        return self.year == obj.year and self.month == obj.month and self.day == obj.day

    def same_calender_month(self, obj):
        return self.year == obj.year and self.month == obj.month

    def diff_days(self, obj):
        return obj.day - self.day

    def same_calender_year(self, obj):
        return self.year == obj.year

    def diff_years(self, obj):
        return obj.year - self.year

    def diff_months(self, obj):
        return obj.month - self.month


actual_date = MyDate(2,7,2015)
expected_date = MyDate(1,2,2014)

if actual_date < expected_date or actual_date == expected_date:
    print 'The fine is : INR 0'
elif expected_date.same_calender_month(actual_date):
    print 'The fine is : INR ' + str(expected_date.diff_days(actual_date) * 15)
elif expected_date.same_calender_year(actual_date):
    print 'The fine is : INR ' + str(expected_date.diff_months(actual_date) * 500)
else:
    print 'The fine is : INR 1000'
