# OneDrive backup script
This script backup all chosen directories and files into another path, such as OneDrive local path. If a previous backup exists it will be deleted first before backuping. **Be aware that backuping will override files and directories no matter of updates done in destination path**.

## Setup config file
Before running the script you should create and fill the `config.json` file. Create the file inside the script main directory and copy/paste the following content by replacing each values with your own value :
```json
{
    "onedrive-path": "Put your onedrive local path (this is the backup destination path that will be used)",
    "saved-paths": [{
        "path": "the full path of a directory that should be backuped",
        "dest-dirname": "the destination directory wich will store the backup (only directory name not full path)"
    }],
    "backup-directory": "The backup directory wich will store all backuped directories (only directory name not full path)",
    "deep-copy": true
}
```

You can backup more than one directory by also putting them in the "saved-paths" list. If the "deep-copy" parameter is `true`, then all subdirectories and files will be also backuped. By default you should let this parameter equal to `true`.
