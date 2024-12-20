function solution(id_pw, db) {
    const [inputId, inputPw] = id_pw;
    
    for (let i = 0; i < db.length; i++) {
        const [dbId, dbPw] = db[i];
        
        if (dbId === inputId) {
            if (dbPw === inputPw) {
                return "login";
            } else {
                return "wrong pw";
            }
        }
    }
    
    return "fail";
}