# Generated from the Opaige API description, https://opaige.com/api/company/v1/openapi.json (version 2026-11-01). Do not edit by hand.

from typing import Any, Dict, Optional, Union

from .request import Requester


class Operations:
    def __init__(self, http: Requester) -> None:
        self._http = http

    def list_appointments(self, *, date: Optional[Union[str, int]] = None) -> Any:
        """A day’s appointments with the file state and the counter stage. GET /appointments"""
        return self._http.request("GET", f"/appointments", query={"date": date})

    def send_appointments(self, *, body: Dict[str, Any]) -> Any:
        """Appointments, from a visa centre’s booking system. POST /appointments"""
        return self._http.request("POST", f"/appointments", query=None, body=body)

    def list_bookings(self, *, updated_since: Optional[Union[str, int]] = None) -> Any:
        """Your bookings with every nudge sent or due. GET /bookings"""
        return self._http.request("GET", f"/bookings", query={"updated_since": updated_since})

    def send_bookings(self, *, body: Dict[str, Any]) -> Any:
        """Bookings, from an airline’s or travel platform’s reservation system: who needs a visa or travel permission, and when each passenger is nudged. POST /bookings"""
        return self._http.request("POST", f"/bookings", query=None, body=body)

    def get_booking(self, *, ref: str) -> Any:
        """One booking by your reference. GET /bookings/{ref}"""
        return self._http.request("GET", f"/bookings/{_q(ref)}", query=None)

    def get_canada_forms(self, *, id: str) -> Any:
        """Where the Canada forms stand on a case, and the forms filed, each with a 10-minute link. GET /cases/{id}/canada-forms"""
        return self._http.request("GET", f"/cases/{_q(id)}/canada-forms", query=None)

    def request_canada_forms(self, *, id: str) -> Any:
        """Queue Canada’s IMM 5257 and IMM 5707 on a case: filled from the case, validated and read back. POST /cases/{id}/canada-forms"""
        return self._http.request("POST", f"/cases/{_q(id)}/canada-forms", query=None)

    def get_case_file(self, *, id: str) -> Any:
        """A case’s finished file, with fresh links. GET /cases/{id}/file"""
        return self._http.request("GET", f"/cases/{_q(id)}/file", query=None)

    def resend_case_file(self, *, id: str) -> Any:
        """Send file.ready again. POST /cases/{id}/file"""
        return self._http.request("POST", f"/cases/{_q(id)}/file", query=None)

    def make_document(self, *, body: Dict[str, Any], format: Optional[Union[str, int]] = None) -> Any:
        """An itinerary, cover letter, submission brief or third-party letter. POST /documents"""
        return self._http.request("POST", f"/documents", query={"format": format}, body=body)

    def review_file(self, *, body: Optional[Dict[str, Any]] = None, file: Optional[bytes] = None, filename: str = "file.pdf", fields: Optional[Dict[str, str]] = None, idempotency_key: Optional[str] = None) -> Any:
        """Every inconsistency in a whole visa file. POST /file-review"""
        return self._http.request("POST", f"/file-review", query=None, body=body, file=file, filename=filename, fields=fields, idempotency_key=idempotency_key)

    def get_file_review(self, *, id: str) -> Any:
        """A review made earlier. GET /file-review/{id}"""
        return self._http.request("GET", f"/file-review/{_q(id)}", query=None)

    def create_upload(self) -> Any:
        """A place to PUT a large PDF before reviewing it. POST /file-review/uploads"""
        return self._http.request("POST", f"/file-review/uploads", query=None)

    def list_ready_files(self, *, since: Optional[Union[str, int]] = None) -> Any:
        """Every file that became ready since a moment: the daily batch. GET /files"""
        return self._http.request("GET", f"/files", query={"since": since})

    def fill_form(self, *, body: Dict[str, Any], format: Optional[Union[str, int]] = None) -> Any:
        """The official visa form, filled from answers. POST /forms"""
        return self._http.request("POST", f"/forms", query={"format": format}, body=body)

    def list_invoices(self, *, status: Optional[Union[str, int]] = None, from_: Optional[Union[str, int]] = None, to: Optional[Union[str, int]] = None) -> Any:
        """Every case billed, due or paid. GET /invoices"""
        return self._http.request("GET", f"/invoices", query={"status": status, "from": from_, "to": to})

    def list_lodgements(self) -> Any:
        """Your lodgements, newest first. GET /lodgements"""
        return self._http.request("GET", f"/lodgements", query=None)

    def create_lodgement(self, *, body: Dict[str, Any], idempotency_key: Optional[str] = None) -> Any:
        """Fill a visa application on the government portal, parked before the declarations (au-600, au-500) or the photo and signature (us-ds160). POST /lodgements"""
        return self._http.request("POST", f"/lodgements", query=None, body=body, idempotency_key=idempotency_key)

    def get_lodgement(self, *, id: str) -> Any:
        """Where a lodgement stands, with the government reference once there is one. GET /lodgements/{id}"""
        return self._http.request("GET", f"/lodgements/{_q(id)}", query=None)

    def attach_lodgement_documents(self, *, id: str, body: Dict[str, Any]) -> Any:
        """Attach supporting documents. POST /lodgements/{id}/documents"""
        return self._http.request("POST", f"/lodgements/{_q(id)}/documents", query=None, body=body)

    def submit_lodgement(self, *, id: str, body: Dict[str, Any], idempotency_key: Optional[str] = None) -> Any:
        """Lodge and pay the government fee (requires authorize: true). POST /lodgements/{id}/submit"""
        return self._http.request("POST", f"/lodgements/{_q(id)}/submit", query=None, body=body, idempotency_key=idempotency_key)

    def lodgement_questions(self, *, visa: Optional[Union[str, int]] = None, purpose: Optional[Union[str, int]] = None) -> Any:
        """The questions a DS-160 lodgement answers, as a case asks them. GET /lodgements/questions"""
        return self._http.request("GET", f"/lodgements/questions", query={"visa": visa, "purpose": purpose})

    def check_passengers(self, *, body: Dict[str, Any]) -> Any:
        """Who on a flight needs a visa, and by when to file. POST /passengers/check"""
        return self._http.request("POST", f"/passengers/check", query=None, body=body)

    def give_passenger_file(self, *, body: Dict[str, Any], idempotency_key: Optional[str] = None) -> Any:
        """Give a passenger their visa file (billed per file). POST /passengers/file"""
        return self._http.request("POST", f"/passengers/file", query=None, body=body, idempotency_key=idempotency_key)

    def get_passenger_settings(self) -> Any:
        """Your page for buying the file, and where passengers get help. GET /passengers/settings"""
        return self._http.request("GET", f"/passengers/settings", query=None)

    def update_passenger_settings(self, *, body: Dict[str, Any]) -> Any:
        """Change them (null clears). PATCH /passengers/settings"""
        return self._http.request("PATCH", f"/passengers/settings", query=None, body=body)

    def passenger_status(self, *, ref: Optional[Union[str, int]] = None) -> Any:
        """Stages of passengers who chose to share. GET /passengers/status"""
        return self._http.request("GET", f"/passengers/status", query={"ref": ref})

    def check_requirements(self, *, passport: Optional[Union[str, int]] = None, destination: Optional[Union[str, int]] = None, residence: Optional[Union[str, int]] = None, stay_days: Optional[Union[str, int]] = None) -> Any:
        """What a passport needs for a destination. GET /requirements"""
        return self._http.request("GET", f"/requirements", query={"passport": passport, "destination": destination, "residence": residence, "stay_days": stay_days})

    def where_to_apply(self, *, residence: Optional[Union[str, int]] = None, destination: Optional[Union[str, int]] = None) -> Any:
        """Who takes the application, where, and who decides it. GET /routes"""
        return self._http.request("GET", f"/routes", query={"residence": residence, "destination": destination})

    def list_rules(self) -> Any:
        """Every destination the rules cover, with versions. GET /rules"""
        return self._http.request("GET", f"/rules", query=None)

    def get_rules(self, *, destination: str) -> Any:
        """One destination: every passport grouped by what it needs, with sources. GET /rules/{destination}"""
        return self._http.request("GET", f"/rules/{_q(destination)}", query=None)

    def list_rule_notices(self, *, since: Optional[Union[str, int]] = None) -> Any:
        """Rule changes announced, in force or coming up. GET /rules/notices"""
        return self._http.request("GET", f"/rules/notices", query={"since": since})

    def list_students(self) -> Any:
        """Admitted students, with the visa stage where each agreed to share it. GET /students"""
        return self._http.request("GET", f"/students", query=None)

    def send_students(self, *, body: Dict[str, Any]) -> Any:
        """Admitted students, from a school’s admissions system; each gets a visa link. POST /students"""
        return self._http.request("POST", f"/students", query=None, body=body)

    def sponsor_compliance(self, *, as_of: Optional[Union[str, int]] = None) -> Any:
        """A UK sponsor’s refusal, enrolment and completion rates as the Basic Compliance Assessment works them. GET /students/compliance"""
        return self._http.request("GET", f"/students/compliance", query={"as_of": as_of})

    def student_funds_check(self, *, body: Dict[str, Any]) -> Any:
        """A student’s money against the study country’s rules (GB, CA, AU, US), each finding with its source. POST /students/funds-check"""
        return self._http.request("POST", f"/students/funds-check", query=None, body=body)

    def list_trips(self, *, status: Optional[Union[str, int]] = None, updated_since: Optional[Union[str, int]] = None) -> Any:
        """Trips and where each case stands. GET /trips"""
        return self._http.request("GET", f"/trips", query={"status": status, "updated_since": updated_since})

    def create_trip(self, *, body: Dict[str, Any]) -> Any:
        """Plan a trip; it follows your approval rules. POST /trips"""
        return self._http.request("POST", f"/trips", query=None, body=body)

    def get_trip(self, *, id: str) -> Any:
        """One trip, with its case. GET /trips/{id}"""
        return self._http.request("GET", f"/trips/{_q(id)}", query=None)

    def get_uptime(self, *, month: Optional[Union[str, int]] = None) -> Any:
        """A month’s measured uptime against the 99.9% commitment. GET /uptime"""
        return self._http.request("GET", f"/uptime", query={"month": month})

    def get_usage(self, *, month: Optional[Union[str, int]] = None) -> Any:
        """This month’s paid API use and what it comes to. GET /usage"""
        return self._http.request("GET", f"/usage", query={"month": month})


def _q(v: str) -> str:
    from urllib.parse import quote
    return quote(str(v), safe="")
