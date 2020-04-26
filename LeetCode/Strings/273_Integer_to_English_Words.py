class Solution:
    def numberToWords(self, num: int) -> str:

        one_digit = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        ten_to_nineteen = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }

        two_digits = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }

        places = {
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }

        def get_three_digit(num):
            """
            Naming for 3 digit numbers
            """
            string = ''
            if not num:
                return string
            hundreds = num // 100
            if hundreds:
                string += '{} {}'.format(one_digit.get(hundreds), 'Hundred')

            last_two = num % 100
            if ten_to_nineteen.get(last_two):
                string += ' ' + ten_to_nineteen.get(last_two)
            else:
                tens_place = last_two // 10
                ones_place = last_two % 10
                if tens_place:
                    string += ' ' + two_digits.get(tens_place)
                if ones_place:
                    string += ' ' + one_digit.get(ones_place)
            return string.strip()

        if num == 0:
            return one_digit.get(0)

        output_str = ''
        place_digit = 0
        while (num):
            three_digits = num % 1000
            str_three_digits = get_three_digit(three_digits)
            if str_three_digits:
                place_str = places.get(place_digit, '')
            else:
                place_str = ''
            num = num // 1000
            place_digit += 1
            output_str = "{} {} {}".format(str_three_digits, place_str,
                                           output_str)
            output_str = output_str.strip()

        return output_str
