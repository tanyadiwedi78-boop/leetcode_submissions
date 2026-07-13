# Reverse Integer

Can you solve this real interview question? Reverse Integer - Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:


Input: x = 123
Output: 321


Example 2:


Input: x = -123
Output: -321

## 💡 Approach

- Extract the last digit of the integer using the modulo (`%`) operator.
- Append the extracted digit to the reversed number by multiplying the current result by 10 and adding the digit.
- Remove the last digit from the original number using integer division.
- Preserve the sign for negative integers.
- Before returning the result, check whether it lies within the 32-bit signed integer range `[-2³¹, 2³¹ - 1]`. If it overflows, return `0`.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** O(log₁₀ n)
- **Space Complexity:** O(1)

---

## 🧠 Key Idea

Reverse the integer digit by digit while ensuring that the final result does not exceed the 32-bit signed integer limit.

---

## 📌 Concepts Used

- Math
- Modulo Operator
- Integer Division
- Overflow Handling

---

##  Interview Takeaways

- Demonstrates digit manipulation without converting the integer to a string.
- Tests understanding of overflow conditions.
- Frequently asked interview problem involving mathematical operations.

---

## 🏷️ Tags

`Math` `Integer` `Simulation` `Medium`


Example 3:


Input: x = 120
Output: 21
