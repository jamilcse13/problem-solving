class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # find out the length of the two strings
        s1_len = len(s1)

        s2_len = len(s2)

        # length of s1 must be be equal or less than length of s2
        if s1_len > s2_len:
            return False

        # find out the volume of chars of s1 and keep it in a dictionary
        count_s1 = dict(Counter(s1))

        # find out the sub-string of length s1 from s2, the volume of chars of s2 and keep it in another dictionary
        s2_str = s2[:s1_len]
        count_s2 = dict(Counter(s2_str))

        # True if both elements volume are same
        if count_s1 == count_s2:
            return True

        for i in range(s1_len, s2_len):
            # remove the first element from sub-string s2
            if count_s2[s2_str[0]] == 1:
                del count_s2[s2_str[0]]
            else:
                count_s2[s2_str[0]] -= 1

            # add next element (using sliding window concept)
            s2_str = s2_str[1:] + s2[i]

            # add the new element count to the s2 sub-string dictionary
            if s2_str[-1] in count_s2:
                count_s2[s2_str[-1]] += 1
            else:
                count_s2[s2_str[-1]] = 1

            # True if both chars volume are same
            if count_s1 == count_s2:
                return True

            # False if complete the iteration and don't get equal elements volume
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
