# User Profile Manager

A Python implementation of a user profile management system with validation and caching mechanisms using descriptor.

## Overview

This project implements a user profile management system that handles user data with built-in validation and efficient caching. It demonstrates the use of Python descriptors, weak references, and property validation.

## Features

- Custom property validation using descriptors
- Automatic cache management using weak references
- Validation for:
  - Username (non-empty string)
  - Email (must contain '@' and '.')
  - Last login timestamp (datetime object or None)
- Automatic cleanup of cached profiles when they're no longer in use

## Components

### UserProfileManager

The main class that handles user profiles with the following validated properties:
- `username`: Must be a non-empty string
- `email`: Must contain '@' and '.' characters
- `last_login`: Must be either a datetime object or None

### ValidatedProperty

A descriptor class that handles property validation and storage.

## Usage 

```python
from user_profile_manager import UserProfileManager
# Create a new profile
profile = UserProfileManager()
# Set valid properties
profile.username = "john_doe"
profile.email = "john@example.com"
profile.last_login = None
# Cache management
UserProfileManager.add_to_cache(profile)
cached_profile = UserProfileManager.get_from_cache(id(profile))
```

## Testing

The project includes comprehensive test cases using pytest. To run the tests:
```bash
pytest test_user_profile_manager.py
```

## Requirements

- Python 3.x
- pytest (for running tests)
- weakref
- datetime

## Project Structure
```
├── user_profile_manager.py # Main implementation
├── test_user_profile_manager.py # Test cases
└── README.md # This file
```
