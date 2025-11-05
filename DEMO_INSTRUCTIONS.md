# GitHub Copilot Coding Agent Demo

This demo shows how to use GitHub Copilot's coding agent to automatically create pull requests in the background.

## Setup Steps

### 1. Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `plan-mode-app` (or your preferred name)
3. **Don't** initialize with README, .gitignore, or license (we already have local files)
4. Click "Create repository"

### 2. Push Your Code to GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/plan-mode-app.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 3. Create a Sample Issue for Copilot to Work On

Once your code is on GitHub, create an issue with one of these example tasks:

**Example Issue 1: Add Logging**
```
Title: Add logging to the Flask application

Description:
Add comprehensive logging to the Flask application:
- Log all incoming requests with timestamps
- Log calculation results
- Log errors with stack traces
- Use Python's logging module
- Configure different log levels (INFO, ERROR)
```

**Example Issue 2: Add POST Endpoint**
```
Title: Add POST endpoint for area calculation

Description:
Create a new POST endpoint at /area that:
- Accepts JSON body with length and width
- Validates the input data
- Returns the area calculation in JSON format
- Includes proper error handling
- Add tests for the new endpoint
```

**Example Issue 3: Add Database Support**
```
Title: Add SQLite database to store calculations

Description:
Implement database functionality:
- Create SQLite database to store calculation history
- Add endpoint to save calculations
- Add endpoint to retrieve calculation history
- Include timestamps for each calculation
```

### 4. Assign the Issue to Copilot (Method 1: From GitHub)

1. Go to your issue on GitHub
2. Click on the issue you created
3. In the issue description or comments, type:
   ```
   @copilot please implement this
   ```
4. Copilot will start working on it in the background!

### 5. Assign the Issue to Copilot (Method 2: From VS Code)

1. Open GitHub Copilot Chat in VS Code (Ctrl+Shift+I or Cmd+Shift+I)
2. Type one of these commands:
   ```
   @workspace /new Create a PR that adds logging to the Flask application with timestamps, error tracking, and different log levels
   ```
   Or:
   ```
   @workspace /new Create a PR that adds a POST endpoint for area calculation accepting JSON input
   ```

3. Copilot will analyze your code and create a pull request on GitHub!

### 6. What Happens Next?

1. **Copilot works in the background**: It uses a GitHub Actions-powered sandbox environment
2. **Creates a branch**: Branch name starts with `copilot/`
3. **Makes changes**: Implements the requested feature
4. **Runs tests**: Executes your existing tests
5. **Opens a PR**: Creates a pull request for your review
6. **Requests review**: Assigns the PR to you

### 7. Review and Iterate

Once Copilot creates the PR:

1. Go to the Pull Requests tab on GitHub
2. Review the changes Copilot made
3. Leave comments if you want changes:
   ```
   @copilot please also add error handling for file I/O operations
   ```
4. Copilot will make additional commits based on your feedback!
5. When satisfied, approve and merge the PR

## Requirements

- ✅ GitHub Copilot Pro, Business, or Enterprise subscription
- ✅ Repository must be hosted on GitHub
- ✅ Copilot coding agent must be enabled (usually enabled by default)

## Benefits of This Approach

- **Asynchronous work**: Copilot works while you focus on other tasks
- **Full transparency**: Every change is tracked in commits
- **Team collaboration**: PRs are visible to the entire team
- **Automated testing**: Copilot runs tests before creating the PR
- **Security scanning**: Built-in checks for secrets, vulnerabilities, etc.

## Try It Now!

Your repository is ready. Follow steps 1-2 above to push to GitHub, then create an issue and assign it to Copilot!
