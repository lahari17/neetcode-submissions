class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for i in strs:
            encode_str = encode_str + str(len(i)) + "#" + i
        return encode_str


    def decode(self, s: str) -> List[str]:
        liststr=[]
        slen = ""
        i=0
        while i<len(s):
            if s[i] == "#":
                length= int(slen)
                slen=""
                liststr.append(s[i+1 : i+length+1])
                i=i+length+1
            else:
                slen=slen+s[i]
                i=i+1
        return liststr

            

