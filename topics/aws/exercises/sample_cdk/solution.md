### Настройка проекта CDK - решение

### Упражнение

Инициализировать проект CDK и подготовить файлы, необходимые для сборки проекта CDK.

### Решение

#### Инициализация проекта CDK

1. Установить CDK на машину командой `npm install -g aws-cdk`.
2. Создать для проекта новый каталог `sample` и выполнить `cdk init app --language typescript`, чтобы инициализировать проект CDK. В качестве языка можно выбрать csharp, fsharp, go, java, javascript, python или typescript.
3. В каталоге будут созданы следующие файлы:
   1. `cdk.json`, `tsconfig.json`, `package.json`  — конфигурационные файлы, задающие глобальные настройки проекта CDK.
   2. `bin/sample.ts` — точка входа проекта CDK. В этом файле определяется стек (stack), который нужно создать.
   3. `lib/sample-stack.ts` — основной файл, в котором будет код проекта CDK.

#### Создание демонстрационной функции lambda

1. В файл `lib/sample-stack.ts` добавить следующий код, создающий функцию lambda:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class SampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const hello = new lambda.Function(this, 'SampleLambda', {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromInline('exports.handler = async () => "hello world";'),
      handler: 'index.handler'
    });
  }
}

```

Будет создана демонстрационная функция lambda, которая при вызове возвращает "hello world".

#### Bootstrap проекта CDK

Перед развёртыванием проекта нужно выполнить для него bootstrap. При этом создаётся стек CloudFormation, который будет использоваться для развёртывания проекта. Выполнить bootstrap можно командой `cdk bootstrap`.

Подробнее о bootstrap — [здесь](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

##### Развёртывание проекта

1. Выполнять `npm install` после каждого изменения, чтобы установить все зависимости проекта.
2. Выполнить `cdk synth`, чтобы синтезировать шаблон CloudFormation для проекта. Появится новый файл `cdk.out/CDKToolkit.template.json` с шаблоном CloudFormation проекта.
3. Выполнить `cdk diff`, чтобы увидеть изменения, которые будут внесены в аккаунт AWS. Будет показан новый стек `SampleStack`, который создаст функцию lambda, и все связанные с этим изменения.
4. Выполнить `cdk deploy`, чтобы развернуть проект. В аккаунте AWS в CloudFormation должен появиться новый стек.
5. Перейти в консоль Lambda — в аккаунте будет создана новая функция lambda `SampleLambda`.

