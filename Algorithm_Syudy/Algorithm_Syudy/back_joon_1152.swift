//
//  back_joon_1152.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2021/08/06.
//

import Foundation

class BackJoon1152 {
    private var wordList: Array<String> = []
    private var answer: Int = 0
    
    
    func signInput() {
        guard let world = readLine() else {return}
        let arr = world.trimmingCharacters(in: .whitespaces).components(separatedBy: " ")
        self.wordList = arr
    }
    func getAnswer() -> Int {
        if self.wordList[0] == "" { return 0}
        self.answer = self.wordList.count
        return self.answer
    }
    
}
