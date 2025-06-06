from wowool.sdk import Pipeline, Domain

FILTER = set(["PersonCompany"])
text = "John Smith works for Ikea."
pipeline = Pipeline("english,entity")

# Define a custom domain with a rule to capture relationships between Person and Company
# Note that you can use the woc compiler to compile bigger domains and add them to your pipeline.
custom_domain = Domain(
    source="""rule:{ Person .. Company } = PersonCompany@(my_rule_att="person->company", person=f"{capture.Person.canonical()}", company=f"{capture.Company.canonical()}");"""
)

document = custom_domain(pipeline(text))
# collect entities and filter bt uri
for e in [e for e in document.entities if e.uri in FILTER]:
    print(
        f"({e.begin_offset:>3},{e.end_offset:>3}): {e.uri:<14}: {e.canonical}\n{' '*12}- attributes : {e.attributes}"
    )
