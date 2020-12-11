//
//  main.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2020/12/11.
//

import Foundation

func bubbleSort(arr: Array<Int>) -> Array<Int> {
    var temp = arr
    let len = arr.count
    var buf = 0
    for i in stride(from: len-1, to: -1, by: -1) {
        for j in stride(from: 0, to: i, by: 1) {
            if temp[j] > temp[j+1] {
                buf = temp[j]
                temp[j] = temp[j+1]
                temp[j+1] = buf
                let p = temp.map({(value) in String(value) })
                print(p.joined(separator: " "))
            }
        }
    }
    return temp
}

var arr =  readLine()!.components(separatedBy: " ").map({ (value) in Int(value)! })
let answer = bubbleSort(arr: arr)


