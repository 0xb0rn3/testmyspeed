# N3tbit - Network Testing & Anonymization Tool

N3tbit is a comprehensive network testing and anonymization tool designed for Linux systems. It provides an intuitive interface for speed testing, network diagnostics, and basic anonymization features through Tor integration.

![N3tbit Banner](screenshots/banner.png)

## Features

N3tbit combines powerful networking tools with a user-friendly interface to provide:

- Network Speed Testing
  - Download speed measurement
  - Upload speed measurement
  - Ping latency testing
  - Persistent results storage
  - Historical data viewing

- Anonymization Features
  - Tor service integration
  - Quick anonymization toggle
  - Connection status monitoring
  - Identity switching

- Cross-Platform Support
  - Compatible with major Linux distributions
  - Automatic dependency resolution
  - System-wide installation

## Installation

### Quick Install

You can install N3tbit directly using curl:

```bash
curl -o netbit https://raw.githubusercontent.com/0xb0rn3/n3tbit/main/netbit
chmod +x netbit
sudo ./netbit --install
```

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/0xb0rn3/n3tbit.git
cd n3tbit
```

2. Make the script executable:
```bash
chmod +x netbit
```

3. Install system-wide:
```bash
sudo ./netbit --install
```

The installation script will automatically:
- Detect your Linux distribution
- Install required dependencies
- Set up necessary directories
- Make the tool accessible system-wide

## Usage

After installation, you can run N3tbit from anywhere in your terminal:

```bash
netbit
```

### Main Menu Options

1. **Full Speed Test**
   - Performs comprehensive network testing
   - Measures download, upload, and ping
   - Saves results for future reference

2. **Download Test Only**
   - Tests download speed independently
   - Useful for quick download performance checks

3. **Upload Test Only**
   - Measures upload speed separately
   - Ideal for testing upload capability

4. **Ping Test Only**
   - Checks network latency
   - Important for gaming and real-time applications

5. **Show Last Results**
   - Displays previous test results
   - Helps track network performance over time

6. **Anonymization Features**
   - Manages Tor service
   - Controls anonymous browsing settings

## Dependencies

N3tbit automatically handles dependencies during installation, but here's what it uses:

- dialog (UI interface)
- speedtest-cli (speed testing)
- curl (network requests)
- tor (anonymization)
- Basic Unix utilities (awk, sed, etc.)

## Configuration

Results are stored in `/var/lib/netbit/speedtest_results.txt` by default. The tool maintains a clean, readable format for all test results.

## Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   sudo chmod +x netbit
   sudo ./netbit --install
   ```

2. **Missing Dependencies**
   ```bash
   # Manually install dialog
   sudo apt-get install dialog  # Debian/Ubuntu
   sudo dnf install dialog      # Fedora
   sudo pacman -S dialog       # Arch
   ```

3. **Results Not Saving**
   ```bash
   # Create directory manually
   sudo mkdir -p /var/lib/netbit
   sudo chmod 777 /var/lib/netbit
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

N3tbit is designed with security in mind, but please be aware:

- Run speed tests on trusted networks
- Keep your system and the tool updated
- Use anonymization features responsibly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created and maintained by [0xb0rn3](https://github.com/0xb0rn3)

## Acknowledgments

- SpeedTest CLI developers
- Tor Project team
- Dialog developers
- Linux distribution maintainers

## Version History

- 2.1: Added Tor integration and improved cross-platform support
- 2.0: Initial public release with speed testing features

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/0xb0rn3/n3tbit).
