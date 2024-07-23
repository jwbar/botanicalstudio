module.exports = {
  apps: [
    {
      name: "botanical-studio",
      script: "mail-form.py",
      interpreter: "python3",
      env: {
        FLASK_ENV: "production",
      },
      cwd: "/var/www/botanical-studio",
    },
  ],
};
