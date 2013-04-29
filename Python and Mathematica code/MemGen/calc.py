'''
Created on Apr 25, 2013

@author: fatestudio
'''
n = 0x44c5b4763fe31d0347fc816ac16e2284c10faa4003ba33db73f7ba8e0445d656de3a5db5154ed51212093d26ac512b01f18dd1eed77c96c0084f3dd6415af341ee52bdb6d1020a15d9ed17e3cc0e95ee8d103ed3cc667e971773308cdc6b13ab2e47dc0e959f3a518cfe5cd12d5db79ba2a7ae1f3ac7652ccdf8440407295e4299901c0475491bc354c56c9a9cc9af4ec9546b439f9d01298a449ebe89d9bf020067dba8589890086a17b9af5b569643d037cdff7c240d4969d495dd81355c53f0e642f43328ad088ded3c9691eb79fa5d5f576cdeb8fc4c7b297d0b0e5e18baf320cd576d14475b349aae908fb5262cc703806984c8199921167d8fcf23cae883333218bd91a1b7f03edca7e2dcaa37f463b337d20b5d59db610487c89da11b62397bc701762741bab9f87ff50592859be3cecb8c497c68a8c24d4244ef7febe8e5b4617589a82b5a702cfa93ea5c4ed8f33418f3d4e7115804f92283868a29678a5aa33b6fe5078c5fe8f8dc3bf364eb8ac8ce8a245e6b33138131c541013d0326324dfb695ffb3a1890c78092b4d42b28fef02b9c014ea5ac06d864c2f2e39403560d97dae38d9d643c25fbb230bbd92a4aa2b410d93c4efbc8d60b21fbac78255d6807923986bb968a437d5c8dfc5eda92d864ac5db9d707107e855c384429e821a4c74803e31ba1621582283d15a9ec0806705fca161622bd795fec898fL
x0 = 0x42cb6d1d
y0 = 0x35f8d170e86384be3c93d362e9a3d31ae106666984bd043bc852925e0f488640a1dcdbc9aca02d5a686d0165d853a24cc4a0cd5e6a29e0bcb7bb09281cf3dac48b94e048a834ba565c9ab30715c7cf2885a2d7c9ab8604ae3410a304899645e3f4cd8f26d452ec9982396676f77186e4ea24d04d7d4eede2ec0f4efa8c21dda62744e146f2ca1780625318d6f43eae1421c9bd4b2ad74ff39b6a0b6de25271e8b6123df6d59a68e902b1da6524c015b21b0100c1ccfcb7c03fd18b649301f9547c1e5552e847480fd257185a34c91ca0fe1f068af8ca97f92356fb988592814bc43fbcc7eca665ed7cdb8062e756c16aa0fb55e36e7717243a3babb908664f99b804c7528f8860bc77b1ce490b3b2dde476672eae45dd36de1d3ca419e00cd9e01bcab2c40c46d3a485bd3777bee866494e7f154646b9a4259f80a0709058b53699bac745d8f560948438abf2f04760105f47c18312d81d5d18a2f46833ebb398523f04eeef4f9e8aed7850a9e52018ac51bfa704bdceebb4d4f07cfa81ed31c1684d7ed8af26000e102491a9412988ff73647d387d30f93f8415e506bf00ded8b7c27c6c6ac811f803eb08b6bbc48752486e972349a04a3830cb7c492a2b38ff00c9137b0feba6badb3aa8446d4547479b85473ce83ff52625f712fe77e5fcbde947c5cd969f724ac4471823dcae8eb2621227dfc9af654ada4ea30aba574bfL
z0 = 0
last_c0 = 0
print(hex(n))

v = x0 * y0 + z0 + last_c0
print("v:")
print(hex(v))

n0_prime = 0xa3b18a91
v0 = 0xb5e88ca3
m = v0 * n0_prime % (2**32)
print("m:")
print(hex(m))

v = v + m * n
print(hex(v))
v = v / (2**32)
print("v:")
print(hex(v))

#n0 = 0x5fec898f
#ans = v0 + m * n0
#print(hex(ans))
#
#ans = v + m * n
#print("vv:")
#print(hex(ans))
#
#a = 17555138354946113191141010309033626261506170611135471526354579215981238085834524547740315849324880781158639249182737547366981179404960923829194416882503485085848182600170715683902659269020498168229402187359487369299193972129197772247141905173302697475832536265048518193930668434175352994376184146558931651303002292987717320706926089312207674911049302498665888188599392584101799552096456267229224488749319106235222906107947625275060164243221291030559243187544269633275025972382150717043095405143910038416311535159461906279370243107425063578323272112035737965461708575574149884779334005006337920179933158918985296826224384473521474735539140964139892957487338467374588961258543587338945796308902111663848726154348875217007564921316789307131918025934771659546984551605715982755963209936979867302211183990738234101411363983648159585194340426689908218758758611436509155181778768859364794260008730241236400517907563749470585822571718510358701601387373501325685612060824814047853843976245211261955398334250472844321554624475555320206753526853222895260720715190400718725066079635005699720190336383345020852905052124227370707133635389457094415022926741814341280786252814913193157076942669884844089932018236043725198465813263226599219621752093
#b = 0xb16ae399ccd3e1f4c2abdaa9c5c11eb3baa17f92c623ac3ad7027cfa358cb1dbe3feafd0e96ed9b5d158e442fcf3b87defa786415ac15c3a217cf253be957670884fd16636abf8ce7e3f52c0cbf404db5c25d429626d8c4344af454f0a61c5e707421d43239d04bcbab5b51385c5fdcbad3116b63b8a8977df0fe6bce8d75f26d62e40c638d521afbc59e92ca1209ad596305b371b221e42fd3b9f2e90f79f835783f662114c2d650ea1324862f78e125c29b6ab575bc6eeee84bcb7281b8a925e4979d6f6ddf79affe2554e5aef699a5e3a7196bf52dfd54a8762b2b12c92c62565a955487b5c3b7626f4975fd35376f1bdd071aff71ae30f2c48549b564fb92a651d7c069c542240397213a082921e695f8baba2338fe4ae302f3b31e9be8a3ef802edf8693ce453432cdffeb5d5f00f520f49ef1c8461dbc24fd0a8aa1e45c7cbc6201a4f7a165264961ab4414aeecb3d561bdf0b015f305ee95afb120f414d4dad6ddfae808afd8643211035083fa999f9b86de3365d8a230de02969326fe2d9d1de377b008641659c078b61daf5afb9565068a3c383739076a9f032cdce32866d30d6a78b07eda9ab9bec60ffe248f4a254cd8ef2471a8c9c60f6ab75bf55b2e5ca6ed0ac07e22e1b7517830328066b49bb1d792a07d25cefb7a0a02ba37cf80256a447a90be0a5a5679009c61a1d20ebc5aa3892a4c88b9d8ab12fb53L