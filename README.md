## Description

Welcome to the **AI-Powered Band Name Generator**! This fun Python app uses OpenAI's GPT-3.5 to generate creative and unique band names based on your hometown and pet’s name.

## Features

- **AI-powered**: Uses OpenAI's GPT-3.5 (or GPT-4) to generate a creative band name.
- **Interactive**: Takes user inputs like the city they grew up in and their pet’s name to generate a personalized band name.
- **Randomized Prompts**: Allows for a variety of prompt questions to keep the experience fresh and fun.

## Getting Started

### Prerequisites

Make sure you have the following installed:

1. **Python 3.7+**: You can download Python [here](https://www.python.org/downloads/).
2. **OpenAI API Key**: You'll need an OpenAI API key to interact with GPT-3.5 or GPT-4. Get your API key from [OpenAI](https://platform.openai.com/account/api-keys).
3. **Virtual Environment (Optional but recommended)**: You can create a virtual environment to keep dependencies isolated.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/BandNameGenerator.git
   cd BandNameGenerator
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scriptsctivate     # Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root of the project and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Add prompts** in a `prompts.json` file with different questions and templates to randomize the user experience. You can add your own questions or modify the existing ones.

### Usage

Once everything is set up, you can run the generator script:

```bash
python name_generator.py
```

The script will:

1. Prompt you for the name of the city you grew up in and your pet’s name.
2. Generate a band name suggestion using AI.

### Example

```bash
Welcome to the AI-Powered Band Name Generator!

Which city did you grow up in?
Indore
What's the name of your favorite animal companion?
Golden retriever

Your AI-generated band name is:
Indore Golden Retrievers
```

---

## Troubleshooting

### 1. **Rate Limit Exceeded (Error 429)**

If you get a rate limit error, it means you've exceeded the free usage quota. Set up billing at OpenAI for continued access.

For more details on managing your usage, check your [OpenAI Usage Page](https://platform.openai.com/account/usage).

### 2. **ModuleNotFoundError: No module named 'openai'**

If you get a "ModuleNotFound" error, you may need to install the OpenAI library:

```bash
pip install openai
```

### 3. **Missing API Key**

Ensure that your `.env` file contains your API key, and it's being loaded correctly.

---

## Contributing

Feel free to fork the repository and make changes. You can contribute by:

- Adding more prompts or randomization options.
- Improving the AI prompt to make it even more creative.
- Fixing bugs or improving performance.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
