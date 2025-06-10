# lc3-vm

LC-3 虚拟机项目。

## 目录结构

```
lc3-vm/
├── assembler/         # 汇编器相关代码
│   └── assembler.py
├── bin/               # 可执行文件输出目录
│   └── lc3vm
├── build/             # 编译中间文件
├── include/           # 头文件
├── src/               # 源代码
│   ├── main.c
│   └── lc3.c
├── test/              # 测试代码/样例
│   ├── hello.asm
│   ├── hello.s
│   └── hello.obj
├── Makefile           # 构建脚本
├── README.md          # 项目说明
├── LICENSE            # 许可证
└── lc3-vm.md          # 其他文档
```

## 用法

编译：
```bash
make
```

运行：
```bash
./bin/lc3vm <program.obj>
```

## 说明
- 源码位于 `src/`，头文件建议放在 `include/`
- 可执行文件输出到 `bin/`
- 测试/样例文件在 `test/`
- 汇编器脚本在 `assembler/`
- 其他文档和说明见根目录
