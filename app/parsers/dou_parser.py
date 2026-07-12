from typing import List

from bs4 import BeautifulSoup
import logging
from urllib.parse import urlparse

from app.models.domain.vacancy import Vacancy


logger = logging.getLogger(__name__)

class DouParser:
    def parse_vacancy(self, html: str) -> List[Vacancy]:
        soup = BeautifulSoup(html, "html.parser")
        vacancies = []

        items = soup.find_all("li", class_="l-vacancy")

        for item in items:
            try:
                title_elem = item.find("a", class_="vt")
                company_elem = item.find("a", class_="company")

                if not title_elem or not company_elem:
                    continue
                # extract job title and company name
                company_name = company_elem.text.strip()
                job_title = title_elem.text.strip()
                job_url = title_elem.get("href")

                # Extract external_id from the URL
                path = urlparse(job_url).path
                external_id = path.rstrip("/").split("/")[-1]

                # Extract location information
                location_elem = item.find("span", class_="cities")
                location = location_elem.text.strip() if location_elem else ""

                vacancy = Vacancy(
                    external_id=external_id,
                    company=company_name,
                    role=job_title,
                    location=location,
                    source_url=job_url,
                )
                vacancies.append(vacancy)
            except Exception as e:
                logger.error(f"Error parsing vacancy: {e}")
                continue

        return vacancies

    def parse_single_vacancy(self, html: str, base_vacancy: Vacancy) -> Vacancy:
        soup = BeautifulSoup(html, "html.parser")

        description_elem = soup.find("div", class_="b-typo")
        if not description_elem:
            description_elem = soup.find("div", class_="l-vacancy")

        apply = soup.find("a", class_="replied-external")
        apply_link = apply.get("href") if apply else None

        raw_text = description_elem.get_text(separator="\n", strip=True) if description_elem else ""

        base_vacancy.raw_text = raw_text
        base_vacancy.apply_link = apply_link

        return base_vacancy

