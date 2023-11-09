# EducomML Back

## Project Overview
EducomML Back is a Django-based web application designed for educational purposes. It manages user accounts, assessments, instructional elements, and integrates with an external application built as part of a doctored thesis.

## Prerequisites
- Python
- Django
- Any additional dependencies mentioned in the `requirements.txt` file

## Installation
1. Clone the repository: `git clone https://github.com/MtheusWilliam/EducomML_Back.git`
2. Navigate to the project directory: `cd EducomML_Back`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`

## Configuration
- Update configuration settings in the `settings.py` file as needed, including database connections and external application endpoints.

## File Structure
- `accounts`: Manages user authentication and profile information.
- `assessment`: Handles assessment parameters, answers, and question types.
- `core`: Contains core models like concepts, knowledge domains, modules, and instructional elements.
- `media`: Deals with media types, mobile media, and file uploads.
- `prior_knowledge`: Manages prior knowledge relationships.
- `questions`: Handles question types, resolutions, and references.
- `scopo`: Defines the scope of the project.
- `templates`: Stores HTML templates.
- `TypeThreshold`: Manages assessment type thresholds.

## File Upload
- File uploads are handled in the `media` app, allowing users to upload images related to their profiles and mobile media content.

## Integration with External Application
- The project integrates with an external application built as part of a doctored thesis. Details on integration can be found in the relevant parts of the code, particularly in models such as `Assessmentparameter`.

## Usage
- The application provides APIs for user authentication, assessment management, instructional elements, and more. Refer to the API documentation for detailed usage instructions.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.
