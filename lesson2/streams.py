def process(self):
        """
        TODO: Implement the `process` method, as described above.

        :return: int
        """

        count = 0  # How many two-digit numbers the `process` method has added
        # together.
        total = 0  # The running total of sums.

        while count < 10 and total < 200:
            digits = self._stream.read(2)
            if len(digits) < 2:
                break

            count += 1

            n = int(digits)
            total += n

        return count
