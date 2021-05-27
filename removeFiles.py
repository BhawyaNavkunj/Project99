import os
import shutil
import time

def main():

	deletedFoldersCount = 0
	deletedFilesCount = 0

	path = 'Path_to_delete'

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			if seconds >= getFileOrFolderAge(root_folder):

				removeFolder(root_folder)
				deletedFoldersCount += 1 

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= getFileOrFolderAge(folder_path):

						removeFolder(folder_path)
						deletedFoldersCount += 1 

				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= getFileOrFolderAge(file_path):

						removeFile(file_path)
						deletedFilesCount += 1 

		else:

			if seconds >= getFileOrFolderAge(path):

				removeFile(path)
				deletedFilesCount += 1

	else:

		print(f'"{path}" is not found')
		deletedFilesCount += 1 

	print(f"Total folders deleted: {deletedFoldersCount}")
	print(f"Total files deleted: {deletedFilesCount}")


def removeFolder(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the "+path)



def removeFile(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the "+path)


def getFileOrFolderAge(path):

	ctime = os.stat(path).st_ctime

	return ctime


if __name__ == '__main__':
	main()