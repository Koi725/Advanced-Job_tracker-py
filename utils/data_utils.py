# utils/data_utils.py

import hashlib


def deduplicate_jobs(job_list, key_fields=None):
    """
    Remove duplicate job entries based on given key fields (like title + company).
    If key_fields is None, uses entire dict hash.
    """
    seen = set()
    unique_jobs = []

    for job in job_list:
        if key_fields:
            identifier = "-".join(str(job.get(k, "")) for k in key_fields)
        else:
            identifier = str(job)

        hash_key = hashlib.sha256(identifier.encode()).hexdigest()

        if hash_key not in seen:
            seen.add(hash_key)
            unique_jobs.append(job)

    return unique_jobs


def filter_jobs_by_tag(job_list, tags):
    """
    Filter job list by matching any of the user's tags in title or description.
    """
    filtered = []
    for job in job_list:
        combined_text = (
            job.get("title", "") + " " + job.get("description", "")
        ).lower()
        if any(tag.lower() in combined_text for tag in tags):
            filtered.append(job)
    return filtered


def sort_jobs_by_date(job_list, reverse=True):
    """
    Sort job list by 'date_posted' field (ISO 8601 format recommended).
    """
    return sorted(job_list, key=lambda x: x.get("date_posted", ""), reverse=reverse)
