def maskify(cc: str) -> str:
  print(cc)
  if len(cc) < 4:
    return cc
  
  return ''.join(['#' for i in range(len(cc) - 4)]) + cc[-4:]