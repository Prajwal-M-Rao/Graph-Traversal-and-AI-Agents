class Atom:
    def __init__(self, predicate, arguments):
        self.predicate = predicate
        self.arguments = arguments

    def __repr__(self):
        return f"{self.predicate}({', '.join(map(str, self.arguments))})"

class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    def __repr__(self):
        return f"{self.head} :- {', '.join(map(str, self.body))}"

class KnowledgeBase:
    def __init__(self):
        self.atoms = []
        self.rules = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def add_rule(self, rule):
        self.rules.append(rule)

    def __repr__(self):
        return "\n".join(map(str, self.rules + self.atoms))

# Example usage
if __name__ == "__main__":
    # Define predicates
    is_human = "is_human"
    is_mortal = "is_mortal"

    # Create a knowledge base
    kb = KnowledgeBase()

    # Add atoms to the knowledge base
    kb.add_atom(Atom(is_human, ["John"]))
    kb.add_atom(Atom(is_human, ["Socrates"]))
    kb.add_atom(Atom(is_mortal, ["John"]))
    kb.add_atom(Atom(is_mortal, ["Socrates"]))

    # Add rules to the knowledge base
    kb.add_rule(Rule(Atom(is_mortal, ["X"]), [Atom(is_human, ["X"])]))

    # Print knowledge base
    print("Knowledge Base:")
    print(kb)
