# Caesar Cipher Encryption & Decryption

A Python program that encrypts and decrypts messages using the Caesar cipher, a classical substitution encryption technique.

## Overview

The Caesar cipher is one of the simplest encryption techniques. It works by shifting each letter in a message by a specified number of positions in the alphabet.

This program allows users to encrypt or decrypt messages by choosing a custom shifting amount.

## Features

- Encrypts messages using a custom shift value.
- Decrypts previously encrypted messages.
- Supports both uppercase and lowercase letters.
- Preserves spaces, numbers, and special characters.
- Handles alphabet wrapping (e.g., Z → C with a shift of 3).
- Allows users to choose between encryption and decryption.

## How It Works

Each letter is converted into its corresponding numerical character value, shifted by the specified amount, and converted back into a letter.

The modulo operator (`% 26`) ensures that letters stay within the 26-letter English alphabet.

For example:

| Original | Shift | Encrypted |
|---|---|---|
| A | 3 | D |
| H | 3 | K |
| X | 3 | A |
| Z | 3 | C |

### Example

**Encryption:**

```text
Enter a word: HELLO
Enter a shifting amount: 3
Do you want to encrypt or decrypt? (e/d): e

Encrypted message: KHOOR
```

**Decryption:**

```text
Enter a word: KHOOR
Enter a shifting amount: 3
Do you want to encrypt or decrypt? (e/d): d

Decrypted message: HELLO
```

## Technologies Used

- **Python 3**
- Built-in Python functions: `input()`, `ord()`, and `chr()`.
- Mathematical operations: addition, subtraction, and modulo (`%`).
- Conditional statements (`if/else`).

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the Python file:

```bash
python main.py
```

*Note: Replace `main.py` with your actual Python filename if it is different.*

## Limitations

The Caesar cipher is a basic educational encryption technique and is not suitable for protecting sensitive information. Since it has only 25 meaningful shift possibilities, it can be easily broken.

## Project Purpose

This project was developed as part of my DecodeLabs internship tasks to practice Python fundamentals, character encoding, mathematical operations, conditional logic, and basic encryption concepts.

---

**Author:** Ulugbek Bozorboyev  
**Language:** Python
