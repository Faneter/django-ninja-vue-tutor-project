const gradeOptions = [
    {value: 'P1', label: '一年级'},
    {value: 'P2', label: '二年级'},
    {value: 'P3', label: '三年级'},
    {value: 'P4', label: '四年级'},
    {value: 'P5', label: '五年级'},
    {value: 'P6', label: '六年级'},
    {value: 'J1', label: '初一'},
    {value: 'J2', label: '初二'},
    {value: 'J3', label: '初三'},
    {value: 'S1', label: '高一'},
    {value: 'S2', label: '高二'},
    {value: 'S3', label: '高三'}
]

const gradeMap = new Map()
gradeOptions.forEach(gradeOption => {
    gradeMap.set(gradeOption.value, gradeOption.label)
})

const subjectOptions = [
    {value: 'CHI', label: '语文'},
    {value: 'MAT', label: '数学'},
    {value: 'ENG', label: '英语'},
    {value: 'PHI', label: '物理'},
    {value: 'CHE', label: '化学'},
    {value: 'BIO', label: '生物'},
    {value: 'POL', label: '政治'},
    {value: 'HIS', label: '历史'},
    {value: 'GEO', label: '地理'}
]

const subjectMap = new Map()
subjectOptions.forEach(subjectOption => {
    subjectMap.set(subjectOption.value, subjectOption.label)
})

const methodOptions = [
    {value: 'T', label: '学员上门'},
    {value: 'S', label: '家教上门'},
    {value: 'O', label: '线上辅导'}
]

const methodMap = new Map()
methodOptions.forEach(methodOption => {
    methodMap.set(methodOption.value, methodOption.label)
})

const paymentOptions = [
    {value: 'D', label: '按天收费'},
    {value: 'H', label: '按小时收费'},
    {value: 'C', label: '面议'}
]

const paymentMap = new Map()
paymentOptions.forEach(paymentOption => {
    paymentMap.set(paymentOption.value, paymentOption.label)
})

const genderOptions = [
    {value: 'M', label: '男'},
    {value: 'F', label: '女'},
]

const tutorGenderOptions = [
    {value: 'M', label: '男'},
    {value: 'F', label: '女'},
    {value: 'U', label: '不限'},
]

const genderMap = new Map()
tutorGenderOptions.forEach(genderOption => {
    genderMap.set(genderOption.value, genderOption.label)
})

export {gradeOptions, subjectOptions, methodOptions, paymentOptions, genderOptions, tutorGenderOptions};
export {gradeMap, subjectMap, methodMap, paymentMap, genderMap}