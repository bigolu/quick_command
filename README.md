# quick_command
cli for remembering commands

## USAGE

You can add commands with an optional description e.g. "tar -xv -> extract a tar file with verbose output"

`qc add`: add a new command. prompts for the command, then the description

`qc find <cmd>`: list all commands that start with \<cmd\> e.g. `qc find tar` lists all commands starting with 'tar'

`qc find`: prompts for a search string, then lists all commands whose descriptions are similar (fuzzy matching used to determine similarity)

`qc db`: path to file containing commands

`qc list`: list all commands

`qc rm`: remove a command

## INSTALLATION

1. `git clone https://github.com/bigolu/quick_command.git` (doesn't matter where, gonna delete it later)

2. `cd quick_command`

3. `pip install .`

4. `cd .. && rm -rf quick_command`

## CONFIGURATION

- commands are stored in `<home_directory>/.qc-commands.db` by default. set the environment variable `QC_DB_DIR` to the directory where you alternatively want the qc to store the commands. e.g. in your .bashrc add `QC_DB_DIR="~/alternate/folder/"`