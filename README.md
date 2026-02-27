Overview
This project demonstrates the deployment and integration of LocalAI, a locally hosted large language model (LLM), as an AI Assistant. The goal is to provide a private and secure environment for AI operations, ensuring data privacy by avoiding exposure to external servers.

Key Features
Locally Hosted AI: Eliminates the need to rely on cloud-based AI solutions, ensuring sensitive data remains on the user's system.
Customizable Configuration: Supports various models, token limits, and adjustable parameters like temperature for response variability.
Streaming Responses: Implements chunked response streaming for low-latency interaction.
Full Control: Provides transparency and control over AI operations, addressing concerns around Shadow AI and data leakage.

how to start your local AI

docker compose up 

<img width="1668" height="930" alt="image" src="https://github.com/user-attachments/assets/42c17c71-1363-4051-82f9-684d17134fd4" />


Browse to your local AI

<img width="1661" height="875" alt="image" src="https://github.com/user-attachments/assets/07cf7eac-782f-4275-817d-698974b0589f" />

Download PHI-3-MINI

<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/5a64b0a1-990e-456e-8d92-4725e9cf931a" />


A FEW MOMENTS LATER ....I CHANGED MY MODEL TO GEMMA ..GUYS I NEED PC RESOURCES DONATIONS AT THIS POINT..TOO SLOW

Issues you may Face ' running out of file descriptors."

MAdd to /etc/sysctl.conf (or a file in /etc/sysctl.d/ like 99-localai.conf):textfs.inotify.max_user_watches=524288
fs.inotify.max_user_instances=512
fs.inotify.max_queued_events=16384Then sudo sysctl --system to apply.

Also Bump Per-Process Open Files (ulimit)
Check current: ulimit -n (probably 1024).
Temporary (current session):textulimit -n 65535Then restart your docker-compose: docker-compose down && docker-compose up -d

<img width="800" height="868" alt="image" src="https://github.com/user-attachments/assets/2f633740-bd19-4715-a3f8-c35e47309176" />


After LocalAI is running:
Onboard OpenClaw → skip provider → manual config
Edit ~/.openclaw/openclaw.json:JSON{
  "providers": {
    "local": {
      "baseUrl": "http://127.0.0.1:8080/v1",
      "apiKey": "",
      "type": "openai / leave blank",
      "model": "gemma-3-4b-it"
    }
  },
  "agent": { "model": "local/gemma-3-4b-it" }
}
Restart gateway: openclaw gateway restart
