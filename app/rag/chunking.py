def chunk_text(text,chunk_size=700,overlap=100):
    if chunk_size<=0 or overlap<0 or overlap>=chunk_size: raise ValueError("Require chunk_size > overlap >= 0")
    words=text.split(); chunks=[]; start=0
    while start<len(words):
        end=min(start+chunk_size,len(words)); chunks.append(" ".join(words[start:end]))
        if end==len(words): break
        start=end-overlap
    return chunks
