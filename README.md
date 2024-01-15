# Mailman Backend

Welcome to the Mailman backend repository! This is the core engine of the Mailman emailing service, built with the robust Python Django framework. Our goal is to provide a powerful, secure, and personalized mailing experience.

## Features

1. **Bulk Mailing with Custom Attachments and Dynamic Content**: Effortlessly send mass emails with personalized attachments and content tailored to each recipient.

## Core Motives

- **Uncompromised Security**: Your security is our top priority. We never store your login credentials, ensuring that your sensitive information remains in your hands alone.
- **Personalization Magic**: Enhance engagement and conversions by personalizing your emails. Address recipients by name and tailor content to their interests.
- **Data-Driven Success**: Use actionable data to refine your campaigns. Analyze mailing reports to understand what resonates with your audience and iterate for continuous improvement.

## Related Repositories

- [Mailman Frontend](https://github.com/BuildNShip/mailman): The frontend of Mailman, built with React. Explore it for a comprehensive user interface experience.

## Installation

Follow these steps to set up and run the Mailman backend on your local machine. This guide assumes you have a basic understanding of Python and Django.

### Prerequisites

- Python (version 3.x)
- Pip (Python package manager)
- Virtual Environment (recommended)

### Steps

1. **Clone the Repository**
   
   Start by cloning the Mailman backend repository to your local machine.
   ```bash
   git clone https://github.com/YourRepository/mailman-backend.git
   cd mailman-backend

2. **Create a Virtual Environment**

    It's a good practice to create a virtual environment for your Python projects. This isolates your project dependencies from the global Python installation.
<br> <br> To create a virtual environment run:
    ```bash
    python3 -m venv venv
   
    Activate the Virtual Environment
    
    On Windows:
    .\venv\Scripts\activate
    

    On Linux or MacOS::
    source venv/bin/activate

3. **Install Required Packages**

    Install all the dependencies listed in the requirements.txt file.
    ```bash
        pip install -r requirements.txt

4. **Set Up Environment Variables**

    Copy the `.env.sample` file to create your own `.env` file. This file will store your secret keys and other sensitive settings.

   
5. **Run the Server**

    Start the Django development server.
    ```bash
        python manage.py runserver

Your backend should now be running on http://localhost:8000/.

## Contributing

Contributions are always welcome!

Want to contribute to Mailman? Great! Please check out our [Contributing Guidelines](./docs/CONTRIBUTING.md).

## FAQ

Got questions? Check out our [Frequently Asked Questions](./docs/FAQ.md).

## Changelog

Stay updated with the changes and improvements made in Mailman. Visit our [Changelog](CHANGELOG.md).

## Code of Conduct

We are committed to building a welcoming and open community. Please read our [Code of Conduct](./docs/CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](./LICENCE.md) file for details.
