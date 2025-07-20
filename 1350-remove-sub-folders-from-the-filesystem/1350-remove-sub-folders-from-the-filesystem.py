class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically
        folder.sort()
        
        # Initialize the result list with no subfolders
        result = []
        
        # Iterate through the sorted folder list
        for f in folder:
            
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result
