import os

def import_query(sql_folder_path, query_file, **kwargs):
    """
    Import the query string from a .sql file

    Parameters
    ----------
    sql_folder_path: path of the sql folder within the current project work directory
    query_file: name of the file which contains the query string. This file lives inside the sql_folder_path
    **kwargs: additional parameters. It depends on the query written in the query file

    Returns
    -------
    query as string
    """
    
    with open(os.path.join(sql_folder_path, query_file), 'r') as arq:
        lines = arq.read()
    return lines.format(**kwargs)
