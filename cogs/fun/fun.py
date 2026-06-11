import discord
import random

from discord import app_commands
from discord.ext import commands

from config import MAIN_COLOR

class Fun(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

        self.reactions = {

            "Грустить": {
                "solo": "{user} грустит.",
                "target": "{user} грустит из-за {target}.",
                "gifs": [
                    "https://images-ext-1.discordapp.net/external/2VqZrRSFRzwHjh6NJx-bORifJt-wv1JNP66qCJPValU/https/cdn.otakugifs.xyz/gifs/sad/a0cfe9c9354c1c28.gif",
                    "https://images-ext-1.discordapp.net/external/LbHaOXFbRIEsmDwUFkiIIvNklMJ0UU2ktogd39eciJs/https/cdn.otakugifs.xyz/gifs/sad/74da5bbeb48d14e2.gif",
                    "https://images-ext-1.discordapp.net/external/uVu3WTdtiYQorkEiKApgczQCc9AJY6Rp_33kgKh6Rk0/https/cdn.otakugifs.xyz/gifs/sad/b2bff4571db8bc48.gif",
                    "https://images-ext-1.discordapp.net/external/8d4yB1EX7bxkL0-EhlZ-2JykBAYFH96nbnuMMgxnYTg/https/cdn.otakugifs.xyz/gifs/sad/dfc703eac9d961f6.gif",
                    "https://images-ext-1.discordapp.net/external/LLlw7XXzOfj3tRTBdV8YRJ9qqFoECErrGnxMHvdp7pc/https/cdn.otakugifs.xyz/gifs/sad/ec27498de0911184.gif",
                    "https://c.tenor.com/Au00PE7HrxYAAAAC/tenor.gif",
                    "https://c.tenor.com/3srSOnT18PQAAAAC/tenor.gif",
                    "https://c.tenor.com/g95du2NWPi8AAAAC/tenor.gif",
                    "https://c.tenor.com/6EQ2aeffrU0AAAAC/tenor.gif",
                    "https://c.tenor.com/jgFeEkAhK6cAAAAd/tenor.gif",
                    "https://c.tenor.com/Y2hbyxTTD-EAAAAd/tenor.gif",
                    "https://c.tenor.com/_00BCbaD2PsAAAAd/tenor.gif",
                    "https://c.tenor.com/C1IDSw6RSAwAAAAd/tenor.gif",
                    "https://c.tenor.com/wfvt7H8U6RQAAAAd/tenor.gif",
                    "https://c.tenor.com/ecV_fJDGXoAAAAAd/tenor.gif",
                    "https://c.tenor.com/26_GcQVlnU4AAAAd/tenor.gif",
                    "https://media.tenor.com/RY9NX67klacAAAAi/sad-cute.gif",
                    "https://c.tenor.com/Ifjf8kh9xi8AAAAd/tenor.gif",
                    "https://c.tenor.com/lBbouKDhudIAAAAC/tenor.gif",
                    "https://c.tenor.com/8Ob5KEU7vKAAAAAd/tenor.gif",
                    "https://c.tenor.com/aGo0xPeeZwgAAAAC/tenor.gif",
                    "https://c.tenor.com/LRCE-IlHdv4AAAAC/tenor.gif",
                    "https://c.tenor.com/vEcyUvOTLI4AAAAC/tenor.gif",
                    "https://c.tenor.com/KmMC1WRWlhkAAAAC/tenor.gif",
                    "https://c.tenor.com/YjJDRk4dXK0AAAAC/tenor.gif"
                ]
            },

            "Плакать": {
                "solo": "{user} плачет.",
                "target": "{user} плачет из-за {target}.",
                "gifs": [
                    "https://c.tenor.com/Bhq1WZGJfqIAAAAd/tenor.gif",
                    "https://c.tenor.com/JFr2V7UKIW0AAAAC/tenor.gif",
                    "https://c.tenor.com/AsTrA5cKBZMAAAAC/tenor.gif",
                    "https://c.tenor.com/bpyAsnhCJGYAAAAd/tenor.gif",
                    "https://c.tenor.com/oAEU2-znoiIAAAAd/tenor.gif",
                    "https://c.tenor.com/GpLx4a7NaE4AAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/cry/Gzv0pzalJv.gif",
                    "https://cdn.otakugifs.xyz/gifs/cry/c21eb26cd733313e.gif",
                    "https://cdn.otakugifs.xyz/gifs/cry/52d1cf6ce6d0e54d.gif",
                    "https://cdn.otakugifs.xyz/gifs/cry/b0f388b11577256e.gif",
                    "https://c.tenor.com/PAtktzMHcr4AAAAC/tenor.gif",
                    "https://c.tenor.com/n85DUKiUX94AAAAC/tenor.gif",
                    "https://c.tenor.com/p8ooeK3t2MMAAAAC/tenor.gif",
                    "https://c.tenor.com/9NQ6gwp930oAAAAd/tenor.gif",
                    "https://c.tenor.com/lksimsDOMlYAAAAd/tenor.gif",
                    "https://c.tenor.com/BJaI3DuCZZ8AAAAd/tenor.gif",
                    "https://c.tenor.com/Pn4ky3KJRH0AAAAC/tenor.gif",
                    "https://c.tenor.com/4dm_hkfKmeEAAAAC/tenor.gif",
                    "https://c.tenor.com/tv2P7rZjWeoAAAAC/tenor.gif",
                    "https://c.tenor.com/KJQVJpuS1xMAAAAC/tenor.gif",
                    "https://c.tenor.com/s-R26oI4jlgAAAAd/tenor.gif",
                    "https://c.tenor.com/-SWgNT1ZC6AAAAAC/tenor.gif",
                    "https://c.tenor.com/9gfJKZaNYMUAAAAC/tenor.gif",
                    "https://c.tenor.com/2pawKZu4h_oAAAAC/tenor.gif",
                    "https://c.tenor.com/3mscVoYlvOcAAAAd/tenor.gif",
                    "https://c.tenor.com/MbcNbKa0M0wAAAAd/tenor.gif"
                ]
            },

            "Радоватся": {
                "solo": "{user} радуется.",
                "target": "{user} радуется вместе с {target}.",
                "gifs": [
                    "https://c.tenor.com/VRW3rpzMnYIAAAAC/tenor.gif",
                    "https://c.tenor.com/7D5KlIpgC4QAAAAC/tenor.gif",
                    "https://c.tenor.com/D05kuhjm9rUAAAAC/tenor.gif",
                    "https://c.tenor.com/fAS0_kCyse8AAAAC/tenor.gif",
                    "https://c.tenor.com/mN75d4-2fBoAAAAd/tenor.gif",
                    "https://c.tenor.com/bPqRWxKP-6gAAAAC/tenor.gif",
                    "https://c.tenor.com/WbgxbgEQQosAAAAd/tenor.gif",
                    "https://c.tenor.com/Nb3p1BSjiaMAAAAC/tenor.gif",
                    "https://c.tenor.com/tokj8JotEs0AAAAC/tenor.gif",
                    "https://c.tenor.com/L7IJbnj42DoAAAAC/tenor.gif",
                    "https://c.tenor.com/9NG4T3vNSOsAAAAd/tenor.gif",
                    "https://c.tenor.com/2gHyCFXKk-QAAAAC/tenor.gif",
                    "https://c.tenor.com/amb1od_txakAAAAC/tenor.gif",
                    "https://c.tenor.com/yap4C0DT6OwAAAAC/tenor.gif",
                    "https://c.tenor.com/WtzHpqklEiIAAAAC/tenor.gif",
                    "https://c.tenor.com/paaUadWmf8QAAAAC/tenor.gif",
                    "https://c.tenor.com/gu0EZJfpXP8AAAAC/tenor.gif",
                    "https://c.tenor.com/d548PiK-PNQAAAAC/tenor.gif",
                    "https://c.tenor.com/1DQrBWjbjd0AAAAC/tenor.gif",
                    "https://c.tenor.com/6xWQhMn23P0AAAAC/tenor.gif",
                    "https://c.tenor.com/U7l4HnwwmXkAAAAC/tenor.gif",
                    "https://c.tenor.com/3S9l9HzhGVcAAAAC/tenor.gif",
                    "https://c.tenor.com/AAMEFNsRaeEAAAAd/tenor.gif",
                    "https://images-ext-1.discordapp.net/external/R3hT4TaUpO_IvMGPKTbuJWky9rKYga4o6EvrNzTjGWY/https/i.gifer.com/Yk9l.gif",
                    "https://images-ext-1.discordapp.net/external/Cfc1yqt5DSsMiW5xYWQYc8mQ5Q83WKblpFiqYf4I2Po/https/i.gifer.com/Ldb9.gif",
                    "https://images-ext-1.discordapp.net/external/-e0ejJjW-4GD3ufckLB-mSetxj4xBGW3v8E0YBc5pOI/https/i.gifer.com/Gytq.gif",
                    "https://c.tenor.com/Aap5eNaSagYAAAAd/tenor.gif",
                    "https://c.tenor.com/k0H_Uglwa64AAAAd/tenor.gif",
                    "https://c.tenor.com/GvlbeFfL2NwAAAAd/tenor.gif",
                    "https://c.tenor.com/QD7j5dlkBQ8AAAAd/tenor.gif",
                    "https://c.tenor.com/e0zC5IJs238AAAAd/tenor.gif",
                    "https://c.tenor.com/L1YVGCNnPl8AAAAd/tenor.gif"
                ]
            },

            "Злится": {
                "solo": "{user} злится.",
                "target": "{user} злится на {target}.",
                "gifs": [
                    "https://c.tenor.com/KI8wOfAPyagAAAAd/tenor.gif",
                    "https://c.tenor.com/T57DHF17Yr0AAAAd/tenor.gif",
                    "https://c.tenor.com/4ziAn98nMiIAAAAd/tenor.gif",
                    "https://c.tenor.com/9JjBiqaxzdAAAAAd/tenor.gif",
                    "https://c.tenor.com/dApWx0IvxgIAAAAd/tenor.gif",
                    "https://c.tenor.com/5NOR0faA94gAAAAd/tenor.gif",
                    "https://c.tenor.com/mhzppZy8BDUAAAAd/tenor.gif",
                    "https://c.tenor.com/o_Wu1bDASyQAAAAd/tenor.gif",
                    "https://c.tenor.com/G9Dzy2V61kkAAAAd/tenor.gif",
                    "https://c.tenor.com/f3ZQlg1--pUAAAAd/tenor.gif",
                    "https://c.tenor.com/63mAIbDICh4AAAAC/tenor.gif",
                    "https://c.tenor.com/5FJku-oZ9SsAAAAC/tenor.gif",
                    "https://c.tenor.com/TI_2JKNb26UAAAAC/tenor.gif",
                    "https://c.tenor.com/xMFhPvyO7m0AAAAd/tenor.gif",
                    "https://c.tenor.com/6bf2Z6KpwyEAAAAd/tenor.gif",
                    "https://c.tenor.com/pS7NXIeIhkoAAAAC/tenor.gif",
                    "https://c.tenor.com/cYRAeQqpaUMAAAAC/tenor.gif",
                    "https://c.tenor.com/1xiMFy-EPn4AAAAC/tenor.gif",
                    "https://c.tenor.com/uctXlnLUN0sAAAAC/tenor.gif",
                    "https://c.tenor.com/U8vM8y9oJjUAAAAC/tenor.gif"
                ]
            },

            "Любить": {
                "solo": "{user} влюблён(а).",
                "target": "{user} любит {target}.",
                "gifs": [
                    "https://cdn.otakugifs.xyz/gifs/love/ad13109ed6ed7a0d.gif",
                    "https://cdn.otakugifs.xyz/gifs/love/4fa4d3db1f354994.gif",
                    "https://c.tenor.com/jGIWPkdsuXsAAAAd/tenor.gif",
                    "https://c.tenor.com/yx9UxhVPi38AAAAC/tenor.gif",
                    "https://c.tenor.com/coXiYCuuQBsAAAAC/tenor.gif",
                    "https://c.tenor.com/-6BcytfXDk4AAAAC/tenor.gif",
                    "https://c.tenor.com/eXYvwzHVB84AAAAd/tenor.gif",
                    "https://c.tenor.com/xISLlxe-IC4AAAAC/tenor.gif",
                    "https://c.tenor.com/49Anku3CpgYAAAAd/tenor.gif",
                    "https://c.tenor.com/9a889ozmQgoAAAAd/tenor.gif",
                    "https://c.tenor.com/beH9ZCmNPMwAAAAd/tenor.gif",
                    "https://c.tenor.com/k-dkLRrwGz4AAAAd/tenor.gif",
                    "https://c.tenor.com/ojac0Pn5ImsAAAAd/tenor.gif",
                    "https://c.tenor.com/Yr3eTFg1rFUAAAAd/tenor.gif",
                    "https://c.tenor.com/jMD5jcj_mtkAAAAd/tenor.gif"
                ]
            },

            "Боятся": {
                "solo": "{user} боится.",
                "target": "{user} боится {target}.",
                "gifs": [
                    "https://c.tenor.com/RhyxCbENd6YAAAAC/tenor.gif",
                    "https://c.tenor.com/UpmhNTwFPcUAAAAC/tenor.gif",
                    "https://c.tenor.com/UKNb_Bp4uPwAAAAC/tenor.gif",
                    "https://c.tenor.com/jY3fVwtKeV0AAAAC/tenor.gif",
                    "https://c.tenor.com/VTHQ7Qh12scAAAAC/tenor.gif",
                    "https://c.tenor.com/hle4ooNxcx4AAAAd/tenor.gif",
                    "https://c.tenor.com/nEh0yvlMrEgAAAAd/tenor.gif",
                    "https://c.tenor.com/XSV31_HJVoQAAAAd/tenor.gif",
                    "https://c.tenor.com/jY3fVwtKeV0AAAAd/tenor.gif",
                    "https://c.tenor.com/Jo5ApxvZa_QAAAAd/tenor.gif",
                    "https://c.tenor.com/CIIqjLt51JsAAAAd/tenor.gif",
                    "https://c.tenor.com/RhyxCbENd6YAAAAd/tenor.gif",
                    "https://c.tenor.com/R1IUWvBoAK8AAAAd/tenor.gif",
                    "https://c.tenor.com/UUYuLeNpo0gAAAAd/tenor.gif",
                    "https://c.tenor.com/ym91vICOUCoAAAAd/tenor.gif",
                    "https://c.tenor.com/dMYYXdpA93EAAAAd/tenor.gif",
                    "https://c.tenor.com/qJAIpf8kIDEAAAAd/tenor.gif",
                    "https://c.tenor.com/8le85OkbM9wAAAAd/tenor.gif",
                    "https://c.tenor.com/wokqCxzAOtgAAAAd/tenor.gif",
                    "https://c.tenor.com/hXAANHMo5HMAAAAd/tenor.gif"
                ]
            },

            "Подарить подарок": {
                "solo": "{user} хочет кому то подарить подарок.",
                "target": "{user} дарит подарок {target}.",
                "gifs": [
                    "https://c.tenor.com/PSgHvjUYpKgAAAAd/tenor.gif",
                    "https://c.tenor.com/xsK_ARX9s2EAAAAd/tenor.gif",
                    "https://c.tenor.com/19Y82NRflb0AAAAd/tenor.gif",
                    "https://c.tenor.com/znG4Dcmyv_AAAAAd/tenor.gif",
                    "https://c.tenor.com/xxC7k1QFoyUAAAAd/tenor.gif",
                    "https://c.tenor.com/F4g9-zQh91YAAAAd/tenor.gif",
                    "https://c.tenor.com/PF0U6izaofIAAAAd/tenor.gif"
                ]
            },

            "Обнять": {
                "solo": "{user} хочет кого-нибудь обнять.",
                "target": "{user} обнял(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/27tM.gif",
                    "https://i.gifer.com/2QEa.gif",
                    "https://i.gifer.com/YW.gif",
                    "https://i.gifer.com/U9L1.gif",
                    "https://i.gifer.com/13Vc.gif",
                    "https://i.gifer.com/79oD.gif",
                    "https://c.tenor.com/7XWzC1zanigAAAAd/tenor.gif",
                    "https://c.tenor.com/IpGw3LOZi2wAAAAd/tenor.gif",
                    "https://c.tenor.com/SYsRdiK-T7gAAAAd/tenor.gif",
                    "https://c.tenor.com/YyCvANEdkBcAAAAd/tenor.gif",
                    "https://c.tenor.com/k_aLQ7SgD04AAAAd/tenor.gif",
                    "https://c.tenor.com/iA9kCGLSzHIAAAAd/tenor.gif",
                    "https://c.tenor.com/sT6SiJgnrFAAAAAd/tenor.gif",
                    "https://c.tenor.com/ZzraYDaXSjAAAAAd/tenor.gif",
                    "https://c.tenor.com/P4NwjAMzfjMAAAAd/tenor.gif",
                    "https://c.tenor.com/BFmsQg9J1ZMAAAAd/tenor.gif",
                    "https://c.tenor.com/upnGVfzUn6IAAAAd/tenor.gif",
                    "https://c.tenor.com/2bWwi8DhDsAAAAAd/tenor.gif",
                    "https://c.tenor.com/_BspICsnrcYAAAAd/tenor.gif",
                    "https://c.tenor.com/Uow__0DXWloAAAAd/tenor.gif",
                    "https://c.tenor.com/I77M4aWAGk8AAAAd/tenor.gif",
                    "https://c.tenor.com/yMghDOetsPUAAAAd/tenor.gif",
                    "https://c.tenor.com/znURt9fG-KcAAAAd/tenor.gif",
                    "https://c.tenor.com/keasv-Cnh4kAAAAd/tenor.gif",
                    "https://i.gifer.com/72Td.gif",
                    "https://i.gifer.com/B7bp.gif"
                ]
            },

            "Поцеловать": {
                "solo": "{user} хочет кого-нибудь поцеловать.",
                "target": "{user} поцеловал(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/XsqT.gif",
                    "https://i.gifer.com/HgKr.gif",
                    "https://i.gifer.com/Jr4.gif",
                    "https://i.gifer.com/gZ2.gif",
                    "https://i.gifer.com/V3ZR.gif",
                    "https://i.gifer.com/8Uc1.gif",
                    "https://i.gifer.com/PCUi.gif",
                    "https://i.gifer.com/i0I.gif",
                    "https://i.gifer.com/C3GK.gif",
                    "https://i.gifer.com/2lte.gif",
                    "https://i.gifer.com/OICq.gif",
                    "https://i.gifer.com/YQzo.gif",
                    "https://i.gifer.com/YQzo.gif",
                    "https://i.gifer.com/T0lE.gif",
                    "https://i.gifer.com/50Ne.gif",
                    "https://i.gifer.com/AUhu.gif",
                    "https://i.gifer.com/QPB7.gif",
                    "https://i.gifer.com/3wih.gif",
                    "https://i.gifer.com/XrqL.gif",
                    "https://i.gifer.com/HgKr.gif",
                    "https://i.gifer.com/JkmQ.gif",
                    "https://i.gifer.com/XsqT.gif",
                    "https://i.gifer.com/gZ2.gif",
                    "https://i.gifer.com/3a1n.gif",
                    "https://i.gifer.com/G9IU.gif",
                    "https://i.gifer.com/YUbh.gif",
                    "https://i.gifer.com/8R91.gif",
                    "https://i.gifer.com/75mW.gif",
                    "https://i.gifer.com/BuMm.gif",
                    "https://i.gifer.com/EX8g.gif",
                    "https://i.gifer.com/36KV.gif",
                    "https://i.gifer.com/LxDu.gif",
                    "https://i.gifer.com/C7Ei.gif",
                    "https://i.gifer.com/9lRL.gif",
                    "https://i.gifer.com/48qb.gif",
                    "https://c.tenor.com/9u2vmryDP-cAAAAd/tenor.gif",
                    "https://c.tenor.com/YhGc7aQAI4oAAAAd/tenor.gif",
                    "https://c.tenor.com/9u2vmryDP-cAAAAd/tenor.gif",
                    "https://c.tenor.com/SqpFZQfcyEgAAAAd/tenor.gif",
                    "https://c.tenor.com/L-NTpww8HTUAAAAd/tenor.gif",
                    "https://c.tenor.com/nRdyrvS3qa4AAAAd/tenor.gif",
                    "https://c.tenor.com/ebi-Gt7Rr_IAAAAd/tenor.gif",
                    "https://c.tenor.com/fFXn6UF_Dt4AAAAd/tenor.gif",
                    "https://c.tenor.com/lJPu85pBQLEAAAAd/tenor.gif",
                    "https://c.tenor.com/XXYatFKMkyIAAAAd/tenor.gif",
                    "https://c.tenor.com/CdKqpbRdwykAAAAd/tenor.gif",
                    "https://c.tenor.com/jmWMMsDaPKcAAAAd/tenor.gif",
                    "https://c.tenor.com/JdpApI0hbZ8AAAAd/tenor.gif"
                ]
            },

            "Погладить": {
                "solo": "{user} погладил себя",
                "target": "{user} погладил(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/fybn.gif",
                    "https://i.gifer.com/7MOk.gif",
                    "https://i.gifer.com/1tZL.gif",
                    "https://i.gifer.com/85yj.gif",
                    "https://c.tenor.com/rZRQ6gSf128AAAAd/tenor.gif",
                    "https://c.tenor.com/iIZ5BwSuaCQAAAAd/tenor.gif",
                    "https://c.tenor.com/EdRtJzbSSRcAAAAd/tenor.gif",
                    "https://c.tenor.com/R9KmpMkjmaIAAAAd/tenor.gif",
                    "https://c.tenor.com/MDc4TSck5PQAAAAd/tenor.gif",
                    "https://c.tenor.com/rtHwrLRPlAkAAAAd/tenor.gif",
                    "https://c.tenor.com/afKzI9a28lIAAAAd/tenor.gif",
                    "https://c.tenor.com/v_2iFqgV904AAAAd/tenor.gif",
                    "https://c.tenor.com/6ZQFPb_cHbwAAAAd/tenor.gif",
                    "https://c.tenor.com/fOqJrM0oieEAAAAd/tenor.gif",
                    "https://c.tenor.com/Jl-9-UGmbowAAAAd/tenor.gif",
                    "https://c.tenor.com/Zm71HaIh7wwAAAAd/tenor.gif",
                    "https://i.gifer.com/FR14.gif",
                    "https://i.gifer.com/7eXV.gif"
                ]
            },

            "Укусить": {
                "solo": "{user} хочет кого-нибудь укусить.",
                "target": "{user} укусил(а) {target}.",
                "gifs": [
                    "https://c.tenor.com/1LtA9dSoAIQAAAAd/tenor.gif",
                    "https://c.tenor.com/n__KGrZPlQEAAAAd/tenor.gif",
                    "https://c.tenor.com/48DDFOcNQBYAAAAd/tenor.gif",
                    "https://c.tenor.com/mXc2f5NeOpgAAAAd/tenor.gif",
                    "https://c.tenor.com/L8GrZ1X6ThsAAAAd/tenor.gif",
                    "https://c.tenor.com/htI5TkSvyYEAAAAd/tenor.gif",
                    "https://c.tenor.com/8UjO54apiUIAAAAd/tenor.gif",
                    "https://c.tenor.com/n__KGrZPlQEAAAAC/tenor.gif",
                    "https://c.tenor.com/JEuY0WWcguIAAAAC/tenor.gif",
                    "https://c.tenor.com/ju5gKmNSdw8AAAAC/tenor.gif",
                    "https://c.tenor.com/ld5vyQrrGXUAAAAC/tenor.gif",
                    "https://i.gifer.com/9fjL.gif",
                    "https://i.gifer.com/np4.gif",
                    "https://i.gifer.com/H3Jt.gif",
                    "https://i.gifer.com/NCMI.gif",
                    "https://c.tenor.com/ECCpi63jZlUAAAAC/tenor.gif"
                ]
            },

            "Смущатся": {
                "solo": "{user} смущается",
                "target": "{user} смущается из-за {target}.",
                "gifs": [
                    "https://i.gifer.com/BHLB.gif",
                    "https://c.tenor.com/3LHHsXREBLIAAAAd/tenor.gif",
                    "https://c.tenor.com/eBtzvs6BwisAAAAd/tenor.gif",
                    "https://c.tenor.com/K3LJM-o3uDwAAAAd/tenor.gif",
                    "https://c.tenor.com/H2ga6sjg76YAAAAd/tenor.gif",
                    "https://c.tenor.com/pSKR-GWjxh4AAAAd/tenor.gif",
                    "https://c.tenor.com/AYBX7n1ts64AAAAd/tenor.gif",
                    "https://c.tenor.com/HyvPjCLtVfYAAAAd/tenor.gif",
                    "https://c.tenor.com/KZybkFnVV8QAAAAd/tenor.gif",
                    "https://c.tenor.com/4zmKrehCzlMAAAAd/tenor.gif",
                    "https://c.tenor.com/RROpU3YUGvYAAAAd/tenor.gif",
                    "https://c.tenor.com/KVyn4i0UWTcAAAAd/tenor.gif",
                    "https://c.tenor.com/trSqsGfka8wAAAAd/tenor.gif",
                    "https://c.tenor.com/FqQImRtClkoAAAAd/tenor.gif",
                    "https://c.tenor.com/T0HIDFIWGWIAAAAd/tenor.gif",
                    "https://c.tenor.com/C9uLsw79b1sAAAAd/tenor.gif",
                    "https://c.tenor.com/XUqWWK7As_gAAAAC/tenor.gif",
                    "https://c.tenor.com/YdX_1WLlaC4AAAAd/tenor.gif",
                    "https://c.tenor.com/huT74g0uC_kAAAAC/tenor.gif",
                    "https://img10.joyreactor.cc/pics/post/Nisekoi-Anime-Kirisaki-Chitoge-3026439.gif",
                    "https://c.tenor.com/huT74g0uC_kAAAAC/tenor.gif"
                ]
            },

            "Дуться": {
                "solo": "{user} дуется",
                "target": "{user} дуется на {target}.",
                "gifs": [
                    "https://c.tenor.com/IU6Zvo4LwDIAAAAC/tenor.gif",
                    "https://c.tenor.com/TiICmBCRvZUAAAAd/tenor.gif",
                    "https://c.tenor.com/_22_7mYKy5EAAAAd/tenor.gif",
                    "https://c.tenor.com/xlwk4diLOPoAAAAd/tenor.gif",
                    "https://c.tenor.com/_FzoXR6YwqEAAAAd/tenor.gif",
                    "https://c.tenor.com/QVwifqbBewcAAAAd/tenor.gif",
                    "https://c.tenor.com/N-QUH4hN-pcAAAAd/tenor.gif",
                    "https://c.tenor.com/4tXvn7g292oAAAAd/tenor.gif",
                    "https://c.tenor.com/dShoDG_n5REAAAAd/tenor.gif"
                ]
            },
            
            "Спать": {
                "solo": "{user} спит",
                "target": "{user} спит вместе с {target}.",
                "gifs": [
                    "https://c.tenor.com/d9AcU5UmEdoAAAAd/tenor.gif",
                    "https://c.tenor.com/dUkiteCccQQAAAAd/tenor.gif",
                    "https://c.tenor.com/oKZVauJ1LWEAAAAd/tenor.gif",
                    "https://c.tenor.com/8DZuAbB5Up0AAAAd/tenor.gif",
                    "https://c.tenor.com/RcXRyLgGcSkAAAAd/tenor.gif",
                    "https://c.tenor.com/DQOy3HfK4-gAAAAd/tenor.gif",
                    "https://c.tenor.com/HnMfryMQ8IEAAAAd/tenor.gif",
                    "https://c.tenor.com/lc_ZdiRuc-4AAAAd/tenor.gif",
                    "https://c.tenor.com/EES7ZFe56w0AAAAd/tenor.gif",
                    "https://c.tenor.com/4jSSY5iIH-MAAAAd/tenor.gif",
                    "https://c.tenor.com/eDVrPUBkx7AAAAAd/tenor.gif",
                    "https://c.tenor.com/RHJyZDF9eC4AAAAd/tenor.gif",
                    "https://c.tenor.com/We9ZtQtm8EwAAAAd/tenor.gif",
                    "https://c.tenor.com/mDn48mryfeMAAAAd/tenor.gif",
                    "https://c.tenor.com/OsJESyCPb1EAAAAd/tenor.gif",
                    "https://c.tenor.com/23NQtnQLhLQAAAAd/tenor.gif",
                    "https://c.tenor.com/qU3p03Cn4ecAAAAd/tenor.gif",
                    "https://c.tenor.com/Bn_E6t9-m_wAAAAd/tenor.gif",
                    "https://c.tenor.com/fKajedt2GVYAAAAd/tenor.gif",
                    "https://c.tenor.com/JTqXUbfSSkYAAAAd/tenor.gif",
                    "https://c.tenor.com/sicZ4NUnxyIAAAAd/tenor.gif",
                    "https://i.gifer.com/3TGw.gif",
                    "https://i.gifer.com/IK9c.gif",
                    "https://i.gifer.com/14t1.gif",
                    "https://i.gifer.com/2m6Y.gif"
                ]
            },

            "Кушать": {
                "solo": "{user} кушает",
                "target": "{user} кушает вместе с {target}.",
                "gifs": [
                    "https://i.gifer.com/HZfw.gif",
                    "https://i.gifer.com/3c9x.gif",
                    "https://i.gifer.com/9bQH.gif",
                    "https://i.gifer.com/RTC.gif",
                    "https://c.tenor.com/LlPM71m6JHMAAAAd/tenor.gif",
                    "https://c.tenor.com/p5DGewKTyQAAAAAd/tenor.gif",
                    "https://c.tenor.com/hlTBlbD8Lp4AAAAd/tenor.gif",
                    "https://c.tenor.com/PtGKgNX9KBcAAAAd/tenor.gif",
                    "https://c.tenor.com/82oMjTNT390AAAAd/tenor.gif",
                    "https://c.tenor.com/0fWSX4-3P2AAAAAd/tenor.gif",
                    "https://c.tenor.com/SmyLNa5WmacAAAAC/tenor.gif",
                    "https://c.tenor.com/PtGKgNX9KBcAAAAC/tenor.gif",
                    "https://c.tenor.com/eleW2f2bhI8AAAAC/tenor.gif",
                    "https://c.tenor.com/p78411-TVP4AAAAd/tenor.gif",
                    "https://c.tenor.com/Y_qbpKEMRPsAAAAC/tenor.gif",
                    "https://c.tenor.com/qhc4J0XIWlYAAAAd/tenor.gif",
                    "https://c.tenor.com/ohM6I9-7LaYAAAAC/tenor.gif",
                    "https://c.tenor.com/i0CPnPA1oyQAAAAC/tenor.gif",
                    "https://c.tenor.com/7NuUEfEvHWoAAAAd/tenor.gif",
                    "https://c.tenor.com/l6Y_KuKoljoAAAAC/tenor.gif"
                ]
            },

            "Ревновать": {
                "solo": "{user} ревнует кого то",
                "target": "{user} ревнует {target} к {target}.",
                "gifs": [
                    "https://c.tenor.com/QVwifqbBewcAAAAd/tenor.gif",
                    "https://c.tenor.com/TiICmBCRvZUAAAAd/tenor.gif",
                    "https://c.tenor.com/iNu8LXx2ECgAAAAd/tenor.gif",
                    "https://c.tenor.com/_22_7mYKy5EAAAAd/tenor.gif",
                    "https://c.tenor.com/xlwk4diLOPoAAAAd/tenor.gif",
                    "https://c.tenor.com/_FzoXR6YwqEAAAAd/tenor.gif",
                    "https://c.tenor.com/KI8wOfAPyagAAAAd/tenor.gif",
                    "https://c.tenor.com/N-QUH4hN-pcAAAAd/tenor.gif",
                    "https://c.tenor.com/6bf2Z6KpwyEAAAAd/tenor.gif",
                    "https://c.tenor.com/pbqNBWOx6xUAAAAd/tenor.gif",
                    "https://c.tenor.com/6DSwiWliBAcAAAAd/tenor.gif",
                    "https://c.tenor.com/EH0Y9GyBHukAAAAd/tenor.gif",
                    "https://c.tenor.com/oQkJcrHLAx0AAAAd/tenor.gif"
                ]
            },

            "Ударить": {
                "solo": "{user} хочет кого то ударить.",
                "target": "{user} ударил(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/7vXk.gif",
                    "https://i.gifer.com/B7sk.gif",
                    "https://i.gifer.com/9eUJ.gif",
                    "https://i.gifer.com/8DpL.gif",
                    "https://i.gifer.com/BlpF.gif",
                    "https://i.gifer.com/1vjb.gif",
                    "https://i.gifer.com/9eUJ.gif",
                    "https://i.gifer.com/B7sk.gif",
                    "https://i.gifer.com/C32F.gif",
                    "https://i.gifer.com/f4.gif",
                    "https://i.gifer.com/3Qwj.gif",
                    "https://i.gifer.com/7RHv.gif",
                    "https://i.gifer.com/C6OC.gif",
                    "https://i.gifer.com/7zBH.gif",
                    "https://c.tenor.com/FJsjk_9b_XgAAAAd/tenor.gif",
                    "https://c.tenor.com/tlgJzKeIlJkAAAAd/tenor.gif",
                    "https://c.tenor.com/p-RMgSXHMCIAAAAd/tenor.gif",
                    "https://c.tenor.com/XLrTcljAp3YAAAAd/tenor.gif",
                    "https://c.tenor.com/D6Ln3UPAdKcAAAAd/tenor.gif",
                    "https://c.tenor.com/YIg9gYzSq7kAAAAd/tenor.gif",
                    "https://c.tenor.com/bO1H2Zv_5doAAAAd/tenor.gif",
                    "https://c.tenor.com/SwMgGqBirvcAAAAd/tenor.gif",
                    "https://c.tenor.com/EiFGi9dZXSAAAAAd/tenor.gif",
                    "https://c.tenor.com/Lyqfq7_vJnsAAAAd/tenor.gif"
                ]
            },

            "Умилятся": {
                "solo": "{user} умиляется",
                "target": "{user} умиляется с {target}.",
                "gifs": [
                    "https://i.gifer.com/Bo6E.gif",
                    "https://i.gifer.com/2q3j.gif",
                    "https://i.gifer.com/YVVM.gif",
                    "https://i.gifer.com/6mh.gif",
                    "https://c.tenor.com/_l1qHrXWKqEAAAAd/tenor.gif",
                    "https://c.tenor.com/-6BcytfXDk4AAAAd/tenor.gif",
                    "https://c.tenor.com/pZ7D-VgpMdIAAAAd/tenor.gif",
                    "https://c.tenor.com/xzrUBUJmd3oAAAAd/tenor.gif",
                    "https://c.tenor.com/VbLL3H2Z4RsAAAAd/tenor.gif"
                ]
            },

            "Удивлятся": {
                "solo": "{user}удивляется",
                "target": "{user} удивляется с {target}.",
                "gifs": [
                    "https://i.gifer.com/5D9N.gif",
                    "https://i.gifer.com/DAuh.gif",
                    "https://i.gifer.com/5D9T.gif",
                    "https://c.tenor.com/n6A1Hez97HMAAAAd/tenor.gif",
                    "https://c.tenor.com/LvlZV5uUmFkAAAAd/tenor.gif",
                    "https://c.tenor.com/Cch23-CfDOAAAAAd/tenor.gif",
                    "https://c.tenor.com/smGoXmymPBEAAAAd/tenor.gif",
                    "https://c.tenor.com/EWDW2iSOgzUAAAAd/tenor.gif",
                    "https://c.tenor.com/hGCzNZNt5CYAAAAd/tenor.gif",
                    "https://c.tenor.com/n7hAMlmWlfoAAAAd/tenor.gif",
                    "https://c.tenor.com/fbyOE8CfREYAAAAd/tenor.gif",
                    "https://c.tenor.com/mmNXz0s9UagAAAAd/tenor.gif",
                    "https://c.tenor.com/obB_7KixgO4AAAAd/tenor.gif"
                ]
            },  

            "Умереть": {
                "solo": "{user} умер(ла)",
                "target": "{user} умер(ла) из-за {target}.",
                "gifs": [
                    "https://i.giphy.com/vFJaEwIm4ih8pGSocI.webp",
                    "https://i.gifer.com/3ZvS.gif",
                    "https://c.tenor.com/Zv7u--6y6JwAAAAd/tenor.gif",
                    "https://c.tenor.com/_aMkVJcxClIAAAAC/tenor.gif",
                    "https://c.tenor.com/Dq5XQslvn8QAAAAd/tenor.gif",
                    "https://c.tenor.com/mV2LIwcx7nEAAAAC/tenor.gif",
                    "https://c.tenor.com/eqZoQKorKbwAAAAC/tenor.gif",
                    "https://c.tenor.com/4GfFjwohAYIAAAAd/tenor.gif",
                    "https://c.tenor.com/sfmq3vkSt1wAAAAC/tenor.gif",
                    "https://c.tenor.com/aPIt6NZ11VEAAAAC/tenor.gif",
                    "https://c.tenor.com/aPIt6NZ11VEAAAAC/tenor.gif",
                    "https://i.giphy.com/rwmwAVkVo1vuEZiVls.webp",
                    "https://i.gifer.com/Rk5D.gif"
                ]
            },

            "Молиться": {
                "solo": "{user} молится",
                "target": "{user} молится на {target}.",
                "gifs": [
                    "https://i.giphy.com/q3EdOWqclqbqFItaTJ.webp",
                    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2lyeTBrdnJ5MGZ5cW04NGYzYmczcTYxd2pnZ3BlZTU5dzdsc2huZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4bEig0bZZaN2l1mw7/giphy.gif",
                    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExczhsZGVwa3Q4ZnprN3c4MGt4amtpbGlrZ2Q1ZzNzYWg2Y2hrN3E1biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QevxWZTp79EygJcdxr/giphy.gif",
                    "https://c.tenor.com/mHLSShZ0Hw8AAAAC/tenor.gif",
                    "https://c.tenor.com/GFCvu0WnT4oAAAAd/tenor.gif"
                ]
            },

            "Секс": {
                "solo": "{user} хочет с кем то занятся любовью",
                "target": "{user} занялся(ась) любовью с {target}.",
                "gifs": [
                    "https://i.gifer.com/8LDU.gif",
                    "https://i.gifer.com/8Sbz.gif",
                    "https://i.gifer.com/WDf.gif",
                    "https://i.gifer.com/8oDh.gif",
                    "https://i.gifer.com/CDtQ.gif",
                    "https://i.gifer.com/MvJH.gif",
                    "https://tenor.com/bVz6h.gif",
                    "https://tenor.com/b0axQ.gif",
                    "https://tenor.com/bTip7BBVJDQ.gif",
                    "https://i.gifer.com/9d8J.gif"
                ]
            },

            "Убить": {
                "solo": "{user} хочет кого то убить",
                "target": "{user} убил(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/WqAA.gif",
                    "https://i.gifer.com/WxoH.gif",
                    "https://i.gifer.com/7ODW.gif",
                    "https://i.gifer.com/Uvgq.gif",
                    "https://i.gifer.com/W9e.gif",
                    "https://i.gifer.com/7ti0.gif"
                ]
            },

            "Танцевать": {
                "solo": "{user} танцует",
                "target": "{user} танцует с {target}.",
                "gifs": [
                    "https://i.gifer.com/3SfS.gif",
                    "https://i.gifer.com/8Hcw.gif",
                    "https://i.gifer.com/bQ.gif",
                    "https://i.gifer.com/8UYb.gif",
                    "https://i.gifer.com/9TL4.gif",
                    "https://i.gifer.com/C8Zg.gif",
                    "https://i.gifer.com/C7B5.gif",
                    "https://i.gifer.com/XqNq.gif",
                    "https://i.gifer.com/6Jrf.gif",
                    "https://i.gifer.com/Afdv.gif",
                    "https://i.gifer.com/8TLD.gif",
                    "https://i.gifer.com/8Q8K.gif",
                    "https://i.gifer.com/YEqS.gif",
                    "https://i.gifer.com/Paw.gif",
                    "https://i.gifer.com/3BBF.gif",
                    "https://i.gifer.com/9fjQ.gif",
                    "https://i.gifer.com/3tA6.gif",
                    "https://i.gifer.com/84P1.gif",
                    "https://i.gifer.com/7Ex6.gif",
                    "https://c.tenor.com/0tFy4K1hRLEAAAAd/tenor.gif",
                    "https://c.tenor.com/PdX3X0HrrkYAAAAd/tenor.gif",
                    "https://c.tenor.com/-oNz696UzLwAAAAd/tenor.gif",
                    "https://c.tenor.com/DwcGAeMnaXwAAAAd/tenor.gif",
                    "https://c.tenor.com/3qDTHPuL15sAAAAd/tenor.gif",
                    "https://c.tenor.com/BUCtvMUtgnoAAAAd/tenor.gif",
                    "https://c.tenor.com/n0OToDppVtYAAAAd/tenor.gif"
                ]
            },

            "Воздушный поцелуй": {
                "solo": "{user} отправляет воздушный поцелуй",
                "target": "{user} отправляет воздушный поцелуй {target}.",
                "gifs": [
                    "https://i.gifer.com/32Jm.gif",
                    "https://i.gifer.com/UkQ1.gif",
                    "https://i.gifer.com/6PLh.gif",
                    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3d6eW80cHJxZGk5emY3OXBiMnl2ajQxd3o5b3Q5Y240cmpjemZyciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vBlVyXxvZlEFUoUzzs/giphy.gif",
                    "https://c.tenor.com/bwwggikAMAgAAAAd/tenor.gif",
                    "https://c.tenor.com/azYJDY8yN78AAAAd/tenor.gif",
                    "https://c.tenor.com/yqXUcXLV6gsAAAAC/tenor.gif",
                    "https://c.tenor.com/PD5XZ5zDvq8AAAAd/tenor.gif",
                    "https://c.tenor.com/ZzndFvEP15cAAAAC/tenor.gif",
                    "https://c.tenor.com/xb1sLPwwRScAAAAd/tenor.gif",
                    "https://c.tenor.com/wTnnE8DNEjAAAAAd/tenor.gif",
                    "https://c.tenor.com/SfasqcIIGP0AAAAC/tenor.gif",
                    "https://c.tenor.com/Gv38EiXASmoAAAAd/tenor.gif"
                ]
            },

            "Сказать бе": {
                "solo": "{user} говорит бе",
                "target": "{user} сказал бе {target}.",
                "gifs": [
                    "https://i.gifer.com/NNCc.gif",
                    "https://i.gifer.com/ax.gif",
                    "https://i.gifer.com/Pxg.gif",
                    "https://i.gifer.com/ByO1.gif",
                    "https://cdn.otakugifs.xyz/gifs/bleh/U9JtRUP8q4BM.gif",
                    "https://cdn.otakugifs.xyz/gifs/bleh/156190b65cb0fd19.gif",
                    "https://cdn.otakugifs.xyz/gifs/bleh/wqUS2tzQFApz.gif"
                ]
            },

            "Держать за руку": {
                "solo": "{user} держит себя в руках",
                "target": "{user} держит за руку {target}.",
                "gifs": [
                    "https://i.gifer.com/YaPQ.gif",
                    "https://cdn.otakugifs.xyz/gifs/handhold/a2be9c7cbdb80d5b.gif",
                    "https://cdn.otakugifs.xyz/gifs/handhold/9X6J03OQi6.gif",
                    "https://i.gifer.com/Pxwc.gif",
                    "https://i.gifer.com/9d8Q.gif",
                    "https://i.gifer.com/Y2oI.gif",
                    "https://i.gifer.com/YCIX.gif",
                    "https://i.gifer.com/9d8K.gif",
                    "https://i.gifer.com/9d8M.gif",
                    "https://i.gifer.com/9d8L.gif",
                    "https://i.gifer.com/D7wP.gif",
                    "https://i.gifer.com/9d8P.gif",
                    "https://c.tenor.com/-76rfR0BNTAAAAAd/tenor.gif",
                    "https://c.tenor.com/by71aaUwdkYAAAAC/tenor.gif",
                    "https://c.tenor.com/mckGHbQ7kNMAAAAd/tenor.gif",
                    "https://c.tenor.com/qZ5UWbLAEBAAAAAd/tenor.gif",
                    "https://c.tenor.com/WUZAwo5KFdMAAAAd/tenor.gif",
                    "https://c.tenor.com/4nUPxEI5f60AAAAC/tenor.gif",
                    "https://c.tenor.com/du8B7p54DLcAAAAC/tenor.gif",
                    "https://c.tenor.com/VOHfRXJxgDkAAAAC/tenor.gif",
                    "https://i.giphy.com/iMJwjtL5GLxPYWMob3.webp"
                ]
            },

            "Рукалицо": {
                "solo": "{user} ловит фейспалм..",
                "target": "{user} ловит фейспалм из-за {target}.",
                "gifs": [
                    "https://i.giphy.com/g1ENyDU0VekgM.webp",
                    "https://c.tenor.com/ddev3tyfgAoAAAAC/tenor.gif",
                    "https://c.tenor.com/miK-GklQp2MAAAAC/tenor.gif",
                    "https://i.gifer.com/2haq.gif",
                    "https://cdn.otakugifs.xyz/gifs/facepalm/de2fe17a75556e04.gif",
                    "https://cdn.otakugifs.xyz/gifs/facepalm/5dccdd762b4b3eb3.gif",
                    "https://cdn.otakugifs.xyz/gifs/facepalm/27e21a316754ab79.gif"
                ]
            },

            "Подглядывать": {
                "solo": "{user} подглядывает",
                "target": "{user} подглядывает за {target}.",
                "gifs": [
                    "https://cdn.otakugifs.xyz/gifs/peek/b8f2d1e325fd8280.gif",
                    "https://cdn.otakugifs.xyz/gifs/peek/73143d8ee1e67f84.gif",
                    "https://cdn.otakugifs.xyz/gifs/peek/c8c81d7abcca457f.gif",
                    "https://cdn.otakugifs.xyz/gifs/peek/f6865fd873b211ef.gif",
                    "https://cdn.otakugifs.xyz/gifs/peek/ce149a3d8f58e5f9.gif"
                ]
            },

            "Апплодировать": {
                "solo": "{user} апплодирует",
                "target": "{user} апплодирует {target}.",
                "gifs": [
                    "https://i.gifer.com/3tA9.gif",
                    "https://i.gifer.com/YTXi.gif",
                    "https://i.gifer.com/QYYD.gif",
                    "https://i.gifer.com/9ou5.gif",
                    "https://i.gifer.com/7ddb.gif",
                    "https://i.gifer.com/28yt.gif",
                    "https://i.gifer.com/LJ.gif",
                    "https://i.gifer.com/49vu.gif",
                    "https://c.tenor.com/57gD-gynMDoAAAAC/tenor.gif",
                    "https://c.tenor.com/Dtjxa7rizZYAAAAd/tenor.gif",
                    "https://c.tenor.com/xdj7XE8llU8AAAAC/tenor.gif",
                    "https://c.tenor.com/cx37Wx28FUkAAAAC/tenor.gif",
                    "https://c.tenor.com/7eQrUIpcRfsAAAAC/tenor.gif",
                    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExemdsMDE3b2NsYWY3eWUzYXhzb3NwamRkZ2d2OHVvYWw0Nm5udHM5cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QRMzGhuVfuGPAA2Pg7/giphy.gif",
                    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDQ2YWVybHhjanhxdmcxbHB6YzZqb3Y0b2xyYXE1MnN6YjRrMXZjdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9NbBZw1NyOsEeA8KAT/giphy.gif",
                    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDIzOGlvZ3dpNGw4ZGdjZXY3OWl1b2t6MnNwM2p2cjI1YmV3a2F0MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26gN1ncIQ8aTtJuXS/giphy.gif"
                ]
            },

            "Лизнуть": {
                "solo": "{user} Лизнул(а)",
                "target": "{user} Лизнул(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/8ZwP.gif",
                    "https://i.gifer.com/G1T0.gif",
                    "https://c.tenor.com/gtyeOa6SBKAAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/edc58043ab55ff91.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/68de3278a0041fcf.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/e7796447a4db880a.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/48e0307890a0e714.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/bd93022885fb1d22.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/0c583e8ab3e6b8aa.gif",
                    "https://cdn.otakugifs.xyz/gifs/lick/e54181dbdb539fb6.gif",
                    "https://i.gifer.com/8Zwm.gif"
                ]
            },

            "Сказать ня": {
                "solo": "{user} говорит ня",
                "target": "{user} говорит ня для {target}.",
                "gifs": [
                    "https://i.gifer.com/X8Ui.gif",
                    "https://i.gifer.com/8Vck.gif",
                    "https://i.gifer.com/68fN.gif",
                    "https://i.gifer.com/8VdR.gif",
                    "https://c.tenor.com/Cyzag2c-m_cAAAAC/tenor.gif",
                    "https://c.tenor.com/Y-i50zr1nqwAAAAC/tenor.gif",
                    "https://c.tenor.com/2kTR2kElHbYAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/nyah/3GM2E6mVSvcD.gif",
                    "https://images-ext-1.discordapp.net/external/7g5-_aUIj2mmpizvds8qspPll13xCTblXMk0PPfDLx8/https/cdn.otakugifs.xyz/gifs/nyah/j7PN9fz3RckA.gif",
                    "https://cdn.otakugifs.xyz/gifs/nyah/uxCwAuJ9Ke.gif",
                    "https://cdn.otakugifs.xyz/gifs/nyah/5hyKZ72BZfKL.gif"
                ]
            },

            "Тыкнуть": {
                "solo": "{user} хочет в кого то тыкнуть",
                "target": "{user} тыкнул(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/S00v.gif",
                    "https://i.gifer.com/FK0b.gif",
                    "https://i.gifer.com/HlJ6.gif",
                    "https://i.gifer.com/JQyj.gif",
                    "https://i.gifer.com/bun.gif",
                    "https://i.gifer.com/Lqge.gif",
                    "https://c.tenor.com/NFU6KXm582gAAAAC/tenor.gif",
                    "https://c.tenor.com/y4R6rexNEJIAAAAC/tenor.gif",
                    "https://c.tenor.com/0wPms8tS0eoAAAAC/tenor.gif",
                    "https://c.tenor.com/hAIMw-_f6hYAAAAC/tenor.gif",
                    "https://c.tenor.com/cEZZ8LBsNVcAAAAC/tenor.gif",
                    "https://c.tenor.com/tUZg2zVOJMYAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/poke/7e68001662f53449.gif",
                    "https://cdn.otakugifs.xyz/gifs/poke/e572cc39c9817440.gif",
                    "https://cdn.otakugifs.xyz/gifs/poke/db2fdca3996922ad.gif",
                    "https://images-ext-1.discordapp.net/external/vOFhvH1zR0eqNj03iQM3q2grddtwJsk0dzvaVNYfqWk/https/cdn.otakugifs.xyz/gifs/poke/08002e2d348de3f5.gif",
                    "https://cdn.otakugifs.xyz/gifs/poke/0fac7376e78ccfe4.gif",
                    "https://cdn.otakugifs.xyz/gifs/poke/3U7KzbHzpt.gif",
                    "https://c.tenor.com/m6UTSUBKHW0AAAAC/tenor.gif"
                ]
            },

            "Сказать нет": {
                "solo": "{user} говорит нет",
                "target": "{user} не согласен с {target}.",
                "gifs": [
                    "https://c.tenor.com/JspxwKBM8iwAAAAd/tenor.gif",
                    "https://media.tenor.com/a5G-QLelej0AAAAi/oshi-no-ko-no.gif",
                    "https://c.tenor.com/nIfKxqBUqQQAAAAC/tenor.gif",
                    "https://c.tenor.com/EKBh2n0f4ZwAAAAC/tenor.gif",
                    "https://c.tenor.com/NjHRzEv4dtsAAAAC/tenor.gif",
                    "https://c.tenor.com/PW2agUueuUwAAAAC/tenor.gif",
                    "https://c.tenor.com/REzNL4LDpEsAAAAC/tenor.gif",
                    "https://c.tenor.com/el1y_HRpyGIAAAAC/tenor.gif",
                    "https://c.tenor.com/BIqUsb17ZkQAAAAd/tenor.gif",
                    "https://c.tenor.com/UDzn7Mcr_gwAAAAC/tenor.gif",
                    "https://c.tenor.com/K3s0l9Zu9y8AAAAC/tenor.gif",
                    "https://c.tenor.com/30S2MyziFDkAAAAC/tenor.gif",
                    "https://media.tenor.com/HxQQzzVJzYYAAAAi/cry-sorry.gif",
                    "https://c.tenor.com/a_ykv4JQqNcAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/no/ee25f56bc4044ce9.gif",
                    "https://cdn.otakugifs.xyz/gifs/no/da8139a0f0761722.gif",
                    "https://i.gifer.com/9qzP.gif",
                ]
            },

            "Сказать да": {
                "solo": "{user} говорит да",
                "target": "{user} согласен с {target}.",
                "gifs": [
                    "https://i.gifer.com/g0UF.gif",
                    "https://i.gifer.com/gci.gif",
                    "https://c.tenor.com/dscrHX9CbssAAAAC/tenor.gif",
                    "https://c.tenor.com/WpZ9HVG_48IAAAAC/tenor.gif",
                    "https://c.tenor.com/Ku0nXSmftncAAAAC/tenor.gif",
                    "https://c.tenor.com/tj-w0D12mqkAAAAC/tenor.gif",
                    "https://c.tenor.com/_2dT6aW89tkAAAAC/tenor.gif",
                    "https://c.tenor.com/KWpFVQPCRoYAAAAC/tenor.gif",
                    "https://media.tenor.com/WTWg2AAc7bsAAAAi/masha-roshidere.gif",
                    "https://c.tenor.com/VLpzyHKoLlUAAAAC/tenor.gif",
                    "https://c.tenor.com/c6eQRar74XYAAAAC/tenor.gif",
                    "https://c.tenor.com/XCtbijgVYVoAAAAC/tenor.gif",
                ]
            },

            "Восхищатся": {
                "solo": "{user} восхищается",
                "target": "{user} восхищается {target}.",
                "gifs": [
                    "https://c.tenor.com/pXOWlMSULnoAAAAC/tenor.gif",
                    "https://c.tenor.com/aS5mDvnf5fEAAAAC/tenor.gif",
                    "https://c.tenor.com/tZKJuFInuPQAAAAd/tenor.gif",
                    "https://c.tenor.com/Ztevi8ck1UwAAAAC/tenor.gif",
                    "https://c.tenor.com/5XQDXlQQB7IAAAAC/tenor.gif",
                    "https://c.tenor.com/1DQrBWjbjd0AAAAC/tenor.gif",
                    "https://c.tenor.com/Zd-yRb1G55wAAAAC/tenor.gif",
                    "https://c.tenor.com/C9BygezNDwAAAAAC/tenor.gif",
                    "https://c.tenor.com/aOrLSZ1c3IwAAAAC/tenor.gif",
                ]
            },

            "Злобно смеятся": {
                "solo": "{user} злобно смеется",
                "target": "{user} злобно смеется с {target}.",
                "gifs": [
                    "https://i.gifer.com/N1Eq.gif",
                    "https://i.gifer.com/1AF6.gif",
                    "https://i.gifer.com/1Fdr.gif",
                    "https://i.gifer.com/AgWn.gif",
                    "https://i.gifer.com/14ln.gif",
                    "https://c.tenor.com/1sdb9S0cLjgAAAAC/tenor.gif",
                    "https://c.tenor.com/NeQ6Mqk2m4oAAAAC/tenor.gif",
                    "https://c.tenor.com/TaIzFEOO05MAAAAC/tenor.gif",
                    "https://c.tenor.com/Tl18Ill_jr8AAAAC/tenor.gif",
                    "https://c.tenor.com/6j5bybtXFMEAAAAC/tenor.gif",
                    "https://c.tenor.com/A4lu69yOzL4AAAAC/tenor.gif",
                    "https://c.tenor.com/Q_SHYUU4NccAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/evillaugh/ce2cb23ec35b5afa.gif",
                    "https://cdn.otakugifs.xyz/gifs/evillaugh/8b758bc1c9b67f2a.gif",
                    "https://cdn.otakugifs.xyz/gifs/evillaugh/b6931cac5154e979.gif",
                ]
            },

            "Запутаться": {
                "solo": "{user} запутался",
                "target": "{user} Запутался из-за {target}.",
                "gifs": [
                    "https://c.tenor.com/zoGCSlNH5J4AAAAd/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/confused/f496db3f81b3cfb3.gif",
                    "https://cdn.otakugifs.xyz/gifs/confused/cc25bf41cdb577e4.gif",
                    "https://cdn.otakugifs.xyz/gifs/confused/f8e3af5327975524.gif",
                    "https://c.tenor.com/obB_7KixgO4AAAAC/tenor.gif",
                    "https://c.tenor.com/kEVg4dod34sAAAAC/tenor.gif",
                    "https://c.tenor.com/2ZuUWp5LDfIAAAAC/tenor.gif",
                    "https://c.tenor.com/rsjivVhI6d8AAAAC/tenor.gif",
                    "https://c.tenor.com/_eWC2cUKtyMAAAAC/tenor.gif",
                    "https://c.tenor.com/m3rQgBx3fl8AAAAd/tenor.gif",
                ]
            },

            "Праздновать": {
                "solo": "{user} празднует",
                "target": "{user} празднует с {target}.",
                "gifs": [
                    "https://tenor.com/be3Jc.gif",
                    "https://tenor.com/H573.gif",
                    "https://tenor.com/hoBtKaaggpM.gif",
                    "https://i.gifer.com/O8zb.gif",
                    "https://i.gifer.com/8XLt.gif",
                    "https://i.gifer.com/74fQ.gif",
                    "https://c.tenor.com/XpOVHJWYrckAAAAC/tenor.gif",
                    "https://c.tenor.com/0xz4SrR-NPsAAAAC/tenor.gif",
                    "https://c.tenor.com/U-dCikr2sLIAAAAC/tenor.gif",
                    "https://cdn.otakugifs.xyz/gifs/celebrate/a4cee6028f5fec0e.gif",
                    "https://cdn.otakugifs.xyz/gifs/celebrate/2250bd2042d3a838.gif",
                    "https://cdn.otakugifs.xyz/gifs/celebrate/K4FAdzTq6ydJ.gif",
                    "https://cdn.otakugifs.xyz/gifs/celebrate/058ace7bf9412c28.gif",
                ]
            },

            "Щекотать": {
                "solo": "{user} хочет кого защекотать",
                "target": "{user} защекотал(а) {target}.",
                "gifs": [
                    "https://i.gifer.com/SKql.gif",
                    "https://i.gifer.com/EKas.gif",
                    "https://c.tenor.com/TMwEbOXboRgAAAAC/tenor.gif",
                    "https://c.tenor.com/_Y9CKX1m178AAAAd/tenor.gif",
                    "https://c.tenor.com/L5-ABrIwrksAAAAC/tenor.gif",
                    "https://c.tenor.com/oW9oUdmiQoYAAAAd/tenor.gif",
                    "https://c.tenor.com/jT65qUu0eeEAAAAC/tenor.gif",
                    "https://c.tenor.com/lvurBEDOsukAAAAC/tenor.gif",
                    "https://c.tenor.com/FbrgN1UUM4EAAAAd/tenor.gif",
                ]
            },

            "Спрятаться": {
                "solo": "{user} спрятался(ась)",
                "target": "{user} спретался(ась) от {target}.",
                "gifs": [
                    "https://c.tenor.com/OY5f0otqa8QAAAAC/tenor.gif",
                    "https://i.gifer.com/4A9v.gif",
                    "https://i.gifer.com/sCO.gif",
                    "https://i.gifer.com/Us2.gif",
                    "https://i.gifer.com/8WpH.gif",
                ]
            },

            "Смеятся": {
                "solo": "{user} смеется",
                "target": "{user} смеется с {target}.",
                "gifs": [
                    "https://i.gifer.com/WD3.gif",
                    "https://c.tenor.com/5cHDD4d8RTsAAAAC/tenor.gif",
                    "https://c.tenor.com/hPz901aqMtMAAAAC/tenor.gif",
                    "https://c.tenor.com/vj0l1aOh8gsAAAAC/tenor.gif",
                    "https://c.tenor.com/CG8uhh9CoJcAAAAC/tenor.gif",
                    "https://c.tenor.com/rwmF-6Q5xesAAAAC/tenor.gif",
                    "https://c.tenor.com/0CmFMbcGVKUAAAAC/tenor.gif",
                    "https://c.tenor.com/-q9PZ3xVN2wAAAAC/tenor.gif",
                    "https://c.tenor.com/axSJHc25AFoAAAAC/tenor.gif",
                    "https://c.tenor.com/74Win7VdWDoAAAAC/tenor.gif",
                    "https://c.tenor.com/cHJdBVQE2gIAAAAC/tenor.gif",
                    "https://c.tenor.com/EqrI4CB-grYAAAAC/tenor.gif",
                    "https://c.tenor.com/DaVI4SrbRPwAAAAC/tenor.gif",
                    "https://c.tenor.com/BP9vMzwRSZwAAAAC/tenor.gif",
                    "https://c.tenor.com/jz9aJI4fys4AAAAC/tenor.gif",
                    "https://c.tenor.com/dgJzIYUxgPsAAAAC/tenor.gif",
                    "https://c.tenor.com/H3gghwcTP6wAAAAC/tenor.gif",
                ]
            },

            "Дать_пощечину": {
                "solo": "{user} хочет кому то дать пощёчину",
                "target": "{user} дал(а) пощёчину {target}.",
                "gifs": [
                    "https://i.gifer.com/9Ky5.gif",
                    "https://i.gifer.com/79zo.gif",
                    "https://i.gifer.com/CXfX.gif",
                    "https://i.gifer.com/8Z0s.gif",
                    "https://i.gifer.com/K02.gif",
                    "https://i.gifer.com/1Vbb.gif",
                    "https://i.gifer.com/9Ky5.gif",
                    "https://i.gifer.com/2MrF.gif",
                    "https://i.gifer.com/cCX.gif",
                    "https://i.gifer.com/CXfX.gif",
                    "https://i.gifer.com/9Ky6.gif",
                    "https://i.gifer.com/9Ky6.gif",
                    "https://c.tenor.com/MXZGFeabIIwAAAAC/tenor.gif",
                    "https://c.tenor.com/sacuMyU4lkwAAAAC/tenor.gif",
                    "https://c.tenor.com/BfQ_gFVUyogAAAAC/tenor.gif",
                    "https://c.tenor.com/5jBuDXkDsjYAAAAC/tenor.gif",
                    "https://c.tenor.com/WYmal-WAnksAAAAd/tenor.gif",
                    "https://c.tenor.com/elWBmgJES9YAAAAC/tenor.gif",
                    "https://c.tenor.com/LTY1a1hMYUUAAAAC/tenor.gif",
                ]
            }
        }

    async def reaction_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str
    ):

        return [

            app_commands.Choice(
                name=name,
                value=name
            )

            for name in self.reactions.keys()

            if current.lower() in name.lower()

        ][:25]

    @app_commands.command(
        name="reaction",
        description="Эмоции и действия"
    )
    @app_commands.autocomplete(
        реакция=reaction_autocomplete
    )
    async def reaction(
        self,
        interaction: discord.Interaction,
        реакция: str,
        пользователь: discord.Member = None
    ):

        if реакция not in self.reactions:

            return await interaction.response.send_message(
                "❌ Такой реакции нет.",
                ephemeral=True
            )

        data = self.reactions[реакция]

        if пользователь:

            text = data["target"].format(
                user=interaction.user.mention,
                target=пользователь.mention
            )

        else:

            text = data["solo"].format(
                user=interaction.user.mention
            )

        embed = discord.Embed(
            description=f"**{text}**",
            color=MAIN_COLOR
        )

        if data["gifs"]:

            embed.set_image(
                url=random.choice(
                    data["gifs"]
                )
            )

        await interaction.response.send_message(
            embed=embed
        )

async def setup(bot):

    await bot.add_cog(
        Fun(bot)
    )