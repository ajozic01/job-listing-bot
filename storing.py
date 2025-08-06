import pandas as pd
from config import excel_file


def save_jobs_to_excel(jobs, filename=excel_file):
    """Save jobs to Excel file, avoiding duplicates"""
    try:
        # Try to read existing file
        try:
            existing_df = pd.read_excel(filename)
            existing_urls = existing_df['url'].tolist() if 'url' in existing_df.columns else []
        except FileNotFoundError:
            existing_urls = []
            existing_df = pd.DataFrame()

        # Filter out duplicates - ensure jobs is a list of dictionaries
        new_jobs = []
        for job in jobs:
            if isinstance(job, dict) and 'url' in job and job['url'] not in existing_urls:
                new_jobs.append(job)

        if new_jobs:
            # Create DataFrame from new jobs
            new_df = pd.DataFrame(new_jobs)

            # Combine with existing data if it exists
            if not existing_df.empty:
                updated_df = pd.concat([existing_df, new_df], ignore_index=True)
            else:
                updated_df = new_df

            # Save to Excel
            updated_df.to_excel(filename, index=False)
            return new_jobs

        return []

    except Exception as e:
        print(f"Error saving to Excel: {e}")
        return []