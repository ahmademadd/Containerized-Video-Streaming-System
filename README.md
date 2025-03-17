# Containerized Video Streaming System

_By Ahmad Emad_  
- **YouTube Video**: [Watch Here](https://youtu.be/0OQjFv8q56g)  
- **Documentation**: [Click Here](Containerized-Video-Streaming-System-Report.pdf).
- **Email**: [ahmademad995.ae@gmail.com](mailto:ahmademad995.ae@gmail.com)

## Overview
This project is a **Flask-based Video streaming system / Cloud video storage system.** that allows authenticated users to upload and stream MP4 files. The system is built using **Docker and Docker Compose**, ensuring a modular and scalable microservices architecture. Enabling users to upload videos securely stream and store them on the cloud.

## Features
- **User Authentication:** Secure login system using MySQL and Redis for session management.
- **MP4 Uploading:** Authenticated users can upload MP4 files.
- **Video Streaming:** Uploaded videos can be streamed by authorized users.
- **Database Management:** MySQL stores user credentials and file metadata.
- **Caching:** Redis is used for session storage and metadata caching to optimize performance.
- **Dockerized Deployment:** Each service runs in its own container for easy scaling and management.

## System Architecture
The system consists of the following services:

### **1. Authentication Service**
- Manages user login and session storage.
- Uses Redis for caching authentication data.
- Stores user credentials in MySQL.

### **2. Upload Service**
- Handles MP4 file uploads.
- Saves file metadata in MySQL.
- Stores files in a persistent volume.

### **3. Streaming Service**
- Streams uploaded MP4 files.
- Retrieves file paths from MySQL.
- Ensures access control for secure playback.

### **4. Database Service (MySQL)**
- Manages user authentication and video file metadata.
- Initializes with a provided SQL script.

### **5. Caching Service (Redis)**
- Caches authentication tokens and session data.
- Reduces database queries to improve response time.

## Deployment
### **Prerequisites**
- Docker
- Docker Compose

### **Setup & Running the System**
1. **Clone the repository:**
   ```sh
   git clone https://github.com/ahmademadd/Containerized-Video-Streaming-System
   cd Containerized-Video-Streaming-System
   ```
2. **Build and start the services:**
   ```sh
   docker-compose up --build
   ```
3. **Access the application:**
   - Authentication service: `http://localhost:5000`
   - Upload service: `http://localhost:5001/upload`
   - Streaming service: `http://localhost:5002/stream`

### **Stopping the System**
To stop all running containers:
```sh
docker-compose down
```

## Configuration
The environment variables for MySQL and Redis are defined in `docker-compose.yml`. You can modify them as needed.

## Volume Management
The system uses **Docker volumes** to persist data:
- `videos`: Stores uploaded video files.
- `db-data`: Stores MySQL database files.
- `redis_data`: Stores Redis cached data.

## Security Measures
- Passwords are hashed before storage.
- Sessions are managed securely using Redis.
- Sensitive data is stored in environment variables instead of hardcoding.

## Future Enhancements
- Implementing **role-based access control** for different user permissions.
- Adding **video transcoding** to support multiple resolutions.
- Integrating **cloud storage/CDN** for faster media delivery.
- Enhancing the UI for a better user experience.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For any questions or issues, feel free to open an issue on GitHub or contact [Ahmad Emad] at [ahmademad995.ae@gmail.com].
