# DIMI CLI

DIMI CLI is a command line interface for general use with many commands aimed to make your life easier.

## Installation

install dependencies
```bash
pip install -r requirements.txt
```

add to PATH
```bash
export PATH="$PATH:/path/to/dimi"
```


## Usage

```bash
dimi
```

## List of commands

### General commands
| Command | Description | Usage |
| --- | --- | --- |
| help | Show help message | help |
| exit | Exit the program | exit |
| clear | Clear the screen | clear |

### System commands
| Command | Description | Usage |
| --- | --- | --- |
| sys | Run system commands | sys <command> |
| mem | Show memory usage | mem |
| ip | Show public IP address | ip |

### File management commands
| Command | Description | Usage |
| --- | --- | --- |
| list | List files in current directory | list |
| in | Change directory | in <directory> |
| out | Change directory to parent | out |
| create | Create a file or directory | create <filename> |
| delete | Delete a file or directory | delete <filename> |
| clean | Delete all files in current directory | clean |

### Download commands
| Command | Description | Usage |
| --- | --- | --- |
| yt | Download a video from YouTube | yt mp3/mp4 <url> |
| ig | Download a video from Instagram | ig <url> |


## TODO
- [ ] Add more download commands
- [ ] Add more file management commands
- [ ] Add more system commands
- [ ] Add more download sources
- [ ] Add more file management sources
- [ ] Add more system sources

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
