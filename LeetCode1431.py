#1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []

        for num in candies:
            result.append(num + extraCandies >= maxCandies)

        return result
