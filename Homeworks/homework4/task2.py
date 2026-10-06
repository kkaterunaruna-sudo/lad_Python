dirty = " !@$%(  Руководство   по   веб-фреймворку     Django  . )?<>  "
clean = dirty.strip("!.@$%*()?>< ")
print(clean)
normalized = " ".join(clean.split())
print(normalized)
words = normalized.split()
print(words)
for word in words:
    print(word.capitalize(), end=" ")
