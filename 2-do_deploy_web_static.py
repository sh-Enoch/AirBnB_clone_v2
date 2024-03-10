
from fabric import task, Connection
import os

@task
def do_deploy(c, archive_path, ssh_user, ssh_key):
    # Set the SSH username and key filename
    env.user = ssh_user
    env.key_filename = ssh_key

    # Check if the archive file exists
    if not os.path.exists(archive_path):
        print(f"Archive file '{archive_path}' not found.")
        return False

    # Get the filename from the archive path
    archive_filename = os.path.basename(archive_path)
    # Remove the file extension to get the release folder name
    release_folder = os.path.splitext(archive_filename)[0]

    # Upload the archive to /tmp/ directory on each server
    for host in env.hosts:
        c.put(archive_path, '/tmp/')

        # Uncompress the archive to /data/web_static/releases/<release_folder>
        with Connection(host) as conn:
            conn.sudo(f'mkdir -p /data/web_static/releases/{release_folder}')
            conn.sudo(f'tar -xzf /tmp/{archive_filename} -C /data/web_static/releases/{release_folder}')

            # Delete the archive from the server
            conn.run(f'rm /tmp/{archive_filename}')

            # Delete the existing symbolic link /data/web_static/current
            conn.sudo('rm -f /data/web_static/current')

            # Create a new symbolic link /data/web_static/current linked to the new version
            conn.sudo(f'ln -s /data/web_static/releases/{release_folder} /data/web_static/current')

    return True
