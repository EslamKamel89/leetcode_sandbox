class Solution:
    def simplifyPath(self, path: str) -> str:
        path_sections = path.split("/")
        result = []
        for p in path_sections:
            if p == "":
                continue
            elif p == "..":
                if result:
                    result.pop()
            elif p == ".":
                continue
            else:
                result.append(p)
        result_path = "/".join(result)
        result_path = f"/{result_path}"
        if result_path[-1] == "/":
            result = result[:-1]
        return result_path
