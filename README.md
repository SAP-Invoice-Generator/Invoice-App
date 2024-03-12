<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">INVOICE READING APP</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing
#### Backend And API
We are using PostgreSQL In Supabase and Using FastAPI which can be hosted in your local amchine or services like the following
Render
Vercel
Heroku
or any paid services oyur wish
1. **Set up VirtualEnv:**

   - **Install VirtualEnv:** Open your terminal and run the following command:

     ```bash
     pip install virtualenv
     ```

   - **Create a Virtual Environment:** Navigate to your project directory using the `cd` command in your terminal. Then, create a virtual environment named `venv` using the following command:

     ```bash
     virtualenv venv
     ```

2. **Set Up Supabase:**

   - Create a Supabase account at [https://supabase.com/docs/guides/database/overview](https://supabase.com/docs/guides/database/overview).
   - Follow Supabase's documentation or online tutorials to obtain your Supabase URL and key. These instructions might involve copying them from your Supabase dashboard.

3. **Clone or Download the Project and Set Up Supabase:**

   - Clone the project repository using Git or download the project zip file.
   - Extract the downloaded zip file or clone the repository into your project directory.
   - **Important:** Locate the Supabase configuration folder within the downloaded/cloned project and move it **outside** the virtual environment folder. Virtual environments are meant to isolate project dependencies, and Supabase configuration typically shouldn't be part of that isolation.

4. **Install Required Packages and Create `.env` File:**
    pip install -r requirements.txt
   - **Activate the virtual environment:**
     - **Windows:** Run `venv\Scripts\activate` in your terminal.
     - **macOS/Linux:** Run `source venv/bin/activate` in your terminal.
     or use .\Trial\SupabaseTrial\Scripts\activate  
   - **Install dependencies:** Navigate to the project directory containing the `requirements.txt` file and run:

     ```bash
     pip install -r requirements.txt
     ```

   - **Create a `.env` file:** In your project directory, create a file named `.env` (make sure there's a dot before "env"). Add your Supabase URL and key to this file, each on a separate line, following this format:

     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_key
     ```

     **Important:** Replace `your_supabase_url` and `your_supabase_key` with your actual Supabase credentials. **Never commit the `.env` file to version control** as it contains sensitive information.

5. **Start Your Project:**

   - Run the necessary commands specific to your project for starting the backend and API development. Refer to your project's documentation for these specific commands.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References



