import python

from AssignExpr assign, string s
where assign.getVariable().matches("(?i).*(api|secret|password|auth|token).*") and
      s.matches(".*[A-Za-z0-9-_]+.*")
select assign, "🚨 Hardcoded credential detected: " + assign.getVariable()
